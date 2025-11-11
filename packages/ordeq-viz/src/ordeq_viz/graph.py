import operator
from collections import defaultdict
from dataclasses import dataclass, field
from typing import Any

from ordeq import Node, View
from ordeq._fqn import fqn_to_object_ref  # noqa: PLC2701 private import
from ordeq._graph import NodeGraph, NodeIOGraph  # noqa: PLC2701 private import
from ordeq._io import AnyIO
from ordeq._resolve import Catalog


@dataclass
class NodeData:
    id: int | str
    node: Node
    name: str
    module: str
    inputs: list[int]
    outputs: list[int]
    view: bool
    attributes: dict[str, Any] = field(default_factory=dict)


@dataclass
class IOData:
    id: int
    dataset: AnyIO
    name: str
    type: str
    attributes: dict[str, Any] = field(default_factory=dict)


def _add_io_data(dataset, reverse_lookup, io_data, store: bool) -> int:
    """Add IOData for a dataset to the io_data dictionary.

    Args:
        dataset: the dataset (Input or Output)
        reverse_lookup: a dictionary mapping dataset IDs to names
        io_data: a dictionary to store IOData objects
        store: whether to store the IOData object

    Returns:
        The ID of the dataset in the io_data dictionary.
    """
    dataset_id = hash(dataset)
    if store:
        if dataset_id not in io_data:
            io_data[dataset_id] = IOData(
                id=dataset_id,
                dataset=dataset,
                name=reverse_lookup[dataset_id],
                type=dataset.__class__.__name__,
            )

        # Handle wrapped datasets
        for wrapped_attribute in dataset.references.values():
            for wrapped_dataset in wrapped_attribute:
                wrapped_id = hash(wrapped_dataset)
                if wrapped_id not in io_data:
                    try:
                        name = reverse_lookup[wrapped_id]
                    except KeyError:
                        name = "<anonymous>"

                    io_data[wrapped_id] = IOData(
                        id=wrapped_id,
                        dataset=wrapped_dataset,
                        name=name,
                        type=wrapped_dataset.__class__.__name__,
                    )
    return dataset_id


def _gather_graph(
    nodes: set[Node], ios: Catalog
) -> tuple[dict[str, list[NodeData]], dict[str | None, list[IOData]]]:
    """Build a graph of nodes and datasets from pipeline (set of nodes)

    Args:
        nodes: nodes
        ios: ios

    Returns:
        metadata for nodes (NodeData)
        metadata for ios (IOData)
    """
    graph = NodeIOGraph.from_nodes(nodes)

    reverse_lookup = {
        hash(io): name
        for _, named_io in sorted(ios.items(), key=operator.itemgetter(0))
        for name, io in sorted(named_io.items(), key=operator.itemgetter(0))
    }

    for io in graph.ios:
        io_id = hash(io)
        if io_id not in reverse_lookup:
            reverse_lookup[io_id] = "<anonymous>"

    io_data: dict[int, IOData] = {}

    node_graph = NodeGraph.from_graph(graph)
    ordering = node_graph.topological_ordering

    node_modules = defaultdict(list)
    io_input_modules = defaultdict(set)
    io_output_modules = defaultdict(set)

    for line in ordering:
        inputs = [
            _add_io_data(input_dataset, reverse_lookup, io_data, store=True)
            for input_dataset in line.inputs
        ]
        outputs = [
            _add_io_data(
                output_dataset,
                reverse_lookup,
                io_data,
                store=not isinstance(line, View),
            )
            for output_dataset in line.outputs
        ]
        # TODO: use resolved name on the NamedGraph when available
        node_module = line.func.__module__
        node_data = NodeData(
            id=fqn_to_object_ref((node_module, line.func.__name__)),
            node=line,
            name=line.func.__name__,
            module=node_module,
            inputs=inputs,
            outputs=outputs,
            view=isinstance(line, View),
        )
        for io_id in inputs:
            io_input_modules[io_id].add(node_module)
        if not node_data.view:
            for io_id in outputs:
                io_output_modules[io_id].add(node_module)
        node_modules[node_module].append(node_data)

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

    return {
        node_module: sorted(nodes, key=lambda n: n.id)
        for node_module, nodes in sorted(
            node_modules.items(), key=operator.itemgetter(0)
        )
    }, io_modules_
