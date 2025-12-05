from collections import defaultdict
from collections.abc import Sequence
from dataclasses import dataclass, field
from typing import Any

from ordeq import Node, View
from ordeq._fqn import FQN
from ordeq._graph import NodeGraph
from ordeq._io import AnyIO
from ordeq._nodes import _is_unit


@dataclass
class NodeData:
    id: str
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


class UnknownCounter:
    unknown_ids: dict[int, str]

    def __init__(self) -> None:
        self._count = 0
        self.unknown_ids = {}

    def next_id(self, obj) -> str:
        if obj not in self.unknown_ids:
            current_id = f"unknown_{self._count}"
            self._count += 1
            self.unknown_ids[obj] = current_id
            return current_id
        return self.unknown_ids[obj]


def _add_io_data(
    dataset: AnyIO, io_data, store: bool, unknown_counter: UnknownCounter
) -> str:
    if dataset.is_fq:
        dataset_id = dataset.fqn.ref  # type: ignore[union-attr]
    else:
        dataset_id = unknown_counter.next_id(dataset)

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
                    wrapped_id = wrapped_dataset.fqn.ref  # type: ignore[union-attr]
                else:
                    wrapped_id = unknown_counter.next_id(dataset)

                if wrapped_id not in io_data:
                    io_data[wrapped_id] = IOData(
                        id=wrapped_id,
                        dataset=wrapped_dataset,
                        name=wrapped_dataset._name or "<anonymous>",  # noqa: SLF001
                        type=wrapped_dataset.__class__.__name__,
                    )
    return dataset_id


def _gather_graph(
    nodes: Sequence[Node],
) -> tuple[dict[str, list[NodeData]], dict[str | None, list[IOData]]]:
    node_graph = NodeGraph.from_nodes(nodes)

    io_data: dict[str, IOData] = {}
    unknown_counter = UnknownCounter()

    node_modules = defaultdict(list)
    for line in node_graph.topological_ordering:
        if _is_unit(line):
            continue
        inputs = [
            _add_io_data(
                input_dataset,
                io_data,
                store=True,
                unknown_counter=unknown_counter,
            )
            for input_dataset in line.inputs
        ]
        outputs = [
            _add_io_data(
                output_dataset,
                io_data,
                store=not isinstance(line, View),
                unknown_counter=unknown_counter,
            )
            for output_dataset in line.outputs
        ]

        node_fqn = line.fqn or FQN("unknown", line.func.__name__)

        node_modules[node_fqn.module].append(
            NodeData(
                id=node_fqn.ref,
                node=line,
                name=node_fqn.name,
                module=node_fqn.module,
                inputs=inputs,
                outputs=outputs,
                view=line.type_name == "View",
            )
        )

    io_input_modules = defaultdict(set)
    io_output_modules = defaultdict(set)
    for module_nodes in node_modules.values():
        for node_data in module_nodes:
            for io_id in node_data.inputs:
                io_input_modules[io_id].add(node_data.module)
            if not node_data.view:
                for io_id in node_data.outputs:
                    io_output_modules[io_id].add(node_data.module)

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
