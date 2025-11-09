from collections import defaultdict
from dataclasses import dataclass
from functools import cached_property
from graphlib import TopologicalSorter
from typing import Any, TypeAlias

from ordeq._io import AnyIO
from ordeq._nodes import Node, View

try:
    from typing import Self  # type: ignore[attr-defined]
except ImportError:
    from typing_extensions import Self

NodeIOEdge: TypeAlias = dict[Node | None, dict[AnyIO, list[Node]]]


def _collect_views(nodes_: set[Node]) -> set[View]:
    views: set[View] = set()
    for node in nodes_:
        node_views = set(node.views)
        views |= node_views | _collect_views(node_views)  # type: ignore[arg-type]
    return views


@dataclass(frozen=True)
class BaseGraph:
    resources: set[Any]
    ios: set[AnyIO]
    nodes: set[Node]
    resource_to_inputs: dict[Any, set[AnyIO]]
    input_to_nodes: dict[AnyIO, set[Node]]
    node_to_outputs: dict[Node, set[AnyIO]]
    output_to_resources: dict[AnyIO, set[Any]]

    @classmethod
    def from_nodes(
            cls, nodes: set[Node], patches: dict[AnyIO | View, AnyIO] | None = None
    ):
        # First pass: collect all views
        views = _collect_views(nodes)
        all_nodes = nodes | views

        if patches is None:
            patches = {}
        for view in sorted(views, key=lambda n: n.name):
            patches[view] = view.outputs[0]

        if patches:
            all_nodes = {node._patch_io(patches) for node in all_nodes}  # noqa: SLF001 (private access)

        # Second pass: register resources & IOs:
        resources = set()
        ios = set()
        nodes = set()

        resource_to_inputs: dict[Any, set[AnyIO]] = defaultdict(set)
        input_to_nodes: dict[AnyIO, set[Node]] = defaultdict(set)
        node_to_outputs: dict[Node, set[AnyIO]] = defaultdict(set)
        output_to_resources: dict[AnyIO, set[Any]] = defaultdict(set)

        # Used to detect outputs that write to the same resource
        resource_to_node: dict[Any, Node] = {}

        for node in all_nodes:
            nodes.add(node)
            for io in node.inputs:
                if io.resource:
                    resources.add(io.resource)
                    resource_to_inputs[io.resource].add(io)
                ios.add(io)
                input_to_nodes[io].add(node)
            for io in node.outputs:
                if io.resource:
                    resources.add(io.resource)
                    output_to_resources[io].add(io.resource)
                    if io.resource in resource_to_node:
                        raise ValueError(
                            f"Nodes '{node.name}' and "
                            f"'{resource_to_node[io.resource].name}' "
                            f"both output to resource {io.resource!r}. "
                            f"Nodes cannot output to the same resource."
                        )
                    resource_to_node[io.resource] = node
                ios.add(io)
                node_to_outputs[node].add(io)

        return cls(
            resource_to_inputs=resource_to_inputs,
            input_to_nodes=input_to_nodes,
            node_to_outputs=node_to_outputs,
            output_to_resources=output_to_resources,
            resources=resources,
            ios=ios,
            nodes=nodes,
        )

    @cached_property
    def edges(self) -> dict[Any, Any]:
        return {
            **self.resource_to_inputs,
            **self.input_to_nodes,
            **self.node_to_outputs,
            **self.output_to_resources,
        }

    @cached_property
    def topological_ordering(self) -> tuple[Any, ...]:
        return tuple(
            reversed(tuple(TopologicalSorter(self.edges).static_order()))
        )


@dataclass(frozen=True, repr=False)
class NodeIOGraph:
    """Graph with views, nodes and IOs."""

    input_to_nodes: dict[AnyIO, set[Node]]
    node_to_outputs: dict[Node, set[AnyIO]]
    ios: set[AnyIO]
    nodes: set[Node]

    @classmethod
    def from_nodes(
            cls, nodes: set[Node], patches: dict[AnyIO | View, AnyIO] | None = None
    ) -> Self:
        return cls.from_graph(BaseGraph.from_nodes(nodes, patches))

    @classmethod
    def from_graph(cls, graph: BaseGraph):
        return cls(
            input_to_nodes=graph.input_to_nodes,
            node_to_outputs=graph.node_to_outputs,
            ios=graph.ios,
            nodes=graph.nodes,
        )

    @cached_property
    def edges(self) -> dict[AnyIO | Node, set[AnyIO | Node]]:
        return {**self.input_to_nodes, **self.node_to_outputs}

    @cached_property
    def topological_ordering(self) -> tuple[Any, ...]:
        return tuple(
            reversed(tuple(TopologicalSorter(self.edges).static_order()))
        )

    def __repr__(self) -> str:
        lines: list[str] = []

        io_ids: dict[AnyIO, str] = {}

        def get_io_idx(io_: AnyIO) -> str:
            if io_ not in io_ids:
                io_ids[io_] = f"io-{len(io_ids) + 1}"
            return io_ids[io_]

        for io, nodes in self.input_to_nodes.items():
            io_idx = get_io_idx(io)
            lines.extend(
                f"{io_idx} --> {type(node).__name__}:{node.name}"
                for node in nodes
            )

        for node, outputs in self.node_to_outputs.items():
            lines.extend(
                f"{type(node).__name__}:{node.name} --> {get_io_idx(io)}"
                for io in outputs
            )

        return "\n".join(lines)


@dataclass(frozen=True)
class NodeGraph:
    """Graph where the edges are node -> [node]."""

    edges: dict[Node, set[Node]]
    nodes: set[Node]

    @classmethod
    def from_nodes(cls, nodes: set[Node]) -> Self:
        return cls.from_graph(NodeIOGraph.from_nodes(nodes))

    @classmethod
    def from_graph(cls, graph: NodeIOGraph) -> Self:
        edges: dict[Node, set[Node]] = {node: set() for node in graph.nodes}

        for node, outputs in graph.node_to_outputs.items():
            for output in outputs:
                if output in graph.input_to_nodes:
                    edges[node].update(graph.input_to_nodes[output])

        return cls(edges=edges, nodes=graph.nodes)

    @property
    def sink_nodes(self) -> set[Node]:
        """Finds the sink nodes, i.e., nodes without successors.

        Returns:
            set of the sink nodes
        """
        return {s for s, targets in self.edges.items() if len(targets) == 0}

    @cached_property
    def topological_ordering(self) -> tuple[Node, ...]:
        return tuple(
            reversed(tuple(TopologicalSorter(self.edges).static_order()))
        )

    def __repr__(self) -> str:
        lines: list[str] = []
        for source_node, target_nodes in self.edges.items():
            lines.extend(
                f"{type(source_node).__name__}:{source_node.name} --> "
                f"{type(target_node).__name__}:{target_node.name}"
                for target_node in target_nodes
            )
            if not target_nodes:
                lines.append(
                    f"{type(source_node).__name__}:{source_node.name}"
                )
        return "\n".join(lines)
