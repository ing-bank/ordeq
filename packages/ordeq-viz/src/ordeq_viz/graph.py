from collections import defaultdict
from collections.abc import Sequence
from dataclasses import dataclass, field
from typing import Any

from ordeq import Node, View
from ordeq._fqn import FQN
from ordeq._graph import IOIdentity, NodeGraph
from ordeq._io import AnyIO
from ordeq._resolve import Catalog


@dataclass
class NodeData:
    id: int | str
    node: Node
    name: str
    module: str
    inputs: list[str]
    outputs: list[str]
    view: bool
    attributes: dict[str, Any] = field(default_factory=dict)


@dataclass
class IOData:
    id: str
    dataset: AnyIO
    name: str
    type: str
    attributes: dict[str, Any] = field(default_factory=dict)


n_unknown = 0


def _add_io_data(dataset: AnyIO, io_data, store: bool) -> str:
    """Add IOData for a dataset to the io_data dictionary.

    Args:
        dataset: the dataset (Input or Output)
        io_data: a dictionary to store IOData objects
        store: whether to store the IOData object

    Returns:
        The ID of the dataset in the io_data dictionary.
    """
    global n_unknown  # noqa: PLW0603
    if dataset.is_fq:
        dataset_id = FQN(*dataset._fqn).ref  # noqa: SLF001
    else:
        dataset_id = f"unknown_{n_unknown}"
        n_unknown += 1

    if store:
        if dataset_id not in io_data:
            io_data[dataset_id] = IOData(
                id=dataset_id,
                dataset=dataset,
                name=dataset._name or "<anonymous>",  # noqa: SLF001
                type=dataset.__class__.__name__,
            )

        # Handle wrapped datasets
        for wrapped_attribute in dataset.references.values():
            for wrapped_dataset in wrapped_attribute:
                if wrapped_dataset.is_fq:
                    wrapped_id = FQN(*wrapped_dataset._fqn).ref  # noqa: SLF001
                else:
                    wrapped_id = f"unknown_{n_unknown}"
                    n_unknown += 1

                if wrapped_id not in io_data:
                    io_data[wrapped_id] = IOData(
                        id=wrapped_id,
                        dataset=wrapped_dataset,
                        name=wrapped_dataset._name or "<anonymous>",  # noqa: SLF001
                        type=wrapped_dataset.__class__.__name__,
                    )
    return dataset_id


def _gather_graph(
    nodes: Sequence[Node], ios: Catalog
) -> tuple[dict[str, list[NodeData]], dict[str | None, list[IOData]]]:
    """Build a graph of nodes and datasets from pipeline (set of nodes)

    Args:
        nodes: nodes
        ios: ios

    Returns:
        metadata for nodes (NodeData)
        metadata for ios (IOData)
    """

    node_graph = NodeGraph.from_nodes(nodes)

    io_data: dict[IOIdentity, IOData] = {}

    node_modules = defaultdict(list)
    io_input_modules = defaultdict(set)
    io_output_modules = defaultdict(set)
    for line in node_graph.topological_ordering:
        inputs = [
            _add_io_data(input_dataset, io_data, store=True)
            for input_dataset in line.inputs
        ]
        outputs = [
            _add_io_data(
                output_dataset, io_data, store=not isinstance(line, View)
            )
            for output_dataset in line.outputs
        ]

        node_fqn = line.fqn or FQN(line.func.__module__, line.func.__name__)

        node_data = NodeData(
            id=node_fqn.ref,
            node=line,
            name=node_fqn.name,
            module=node_fqn.module,
            inputs=inputs,
            outputs=outputs,
            view=isinstance(line, View),
        )
        for io_id in inputs:
            io_input_modules[io_id].add(node_fqn.module)
        if not node_data.view:
            for io_id in outputs:
                io_output_modules[io_id].add(node_fqn.module)
        node_modules[node_fqn.module].append(node_data)

    io_modules_ = defaultdict(list)
    for io_id in set(io_input_modules.keys()) | set(io_output_modules.keys()):
        input_modules = io_input_modules.get(io_id, set())
        output_modules = io_output_modules.get(io_id, set())

        module = (
            None
            if len(input_modules) != 1
            or len(output_modules) != 1
            or input_modules != output_modules
            else input_modules.pop()
        )
        io_modules_[module].append(io_data[io_id])

    return node_modules, io_modules_
