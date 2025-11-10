from collections import UserDict, defaultdict
from dataclasses import dataclass
from functools import cached_property
from graphlib import TopologicalSorter
from typing import Any, Generic, TypeAlias, TypeVar

from ordeq._io import AnyIO, get_resource, has_resource
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


T = TypeVar("T")


class OrderedSet(UserDict[T, None]):
    def __init__(self):
        self.data = {}
        super().__init__()

    def add(self, key):
        super().__setitem__(key, None)


Tvertex = TypeVar("Tvertex")


class Graph(Generic[Tvertex]):
    edges: dict[Tvertex, OrderedSet[Tvertex]]

    @cached_property
    def topological_ordering(self) -> tuple[Tvertex, ...]:
        return tuple(
            reversed(tuple(TopologicalSorter(self.edges).static_order()))
        )


@dataclass(frozen=True)
class BaseGraph(Graph[Any]):
    resources: OrderedSet[Any]
    ios: OrderedSet[AnyIO]
    nodes: OrderedSet[Node]
    resource_to_inputs: dict[Any, OrderedSet[AnyIO]]
    input_to_nodes: dict[AnyIO, OrderedSet[Node]]
    node_to_outputs: dict[Node, OrderedSet[AnyIO]]
    output_to_resources: dict[AnyIO, OrderedSet[Any]]

    @classmethod
    def from_nodes(
        cls, nodes: set[Node], patches: dict[AnyIO | View, AnyIO] | None = None
    ) -> Self:
        # First pass: collect all views
        views = _collect_views(nodes)
        all_nodes = nodes | views

        if patches is None:
            patches = {}
        for view in sorted(views, key=lambda n: n.name):
            patches[view] = view.outputs[0]

        if patches:
            all_nodes = {node._patch_io(patches) for node in all_nodes}  # noqa: SLF001 (private access)

        resources = OrderedSet()
        ios = OrderedSet()
        nodes = OrderedSet()

        resource_to_inputs: dict[Any, OrderedSet[AnyIO]] = defaultdict(
            OrderedSet
        )
        input_to_nodes: dict[AnyIO, OrderedSet[Node]] = defaultdict(OrderedSet)
        node_to_outputs: dict[Node, OrderedSet[AnyIO]] = defaultdict(
            OrderedSet
        )
        output_to_resources: dict[AnyIO, OrderedSet[Any]] = defaultdict(
            OrderedSet
        )

        # Used to detect outputs that write to the same resource:
        resource_to_node: dict[Any, Node] = {}

        # Traverse the nodes, sorted by name to preserve determinism:
        for node in sorted(all_nodes, key=lambda node: node.name):
            nodes.add(node)
            for io in node.inputs:
                resource = get_resource(io)
                resources.add(resource)
                resource_to_inputs[resource].add(io)
                ios.add(io)
                input_to_nodes[io].add(node)
            for io in node.outputs:
                resource = get_resource(io)
                resources.add(resource)
                output_to_resources[io].add(resource)
                if has_resource(io) and resource in resource_to_node:
                    raise ValueError(
                        f"Nodes '{node.name}' and "
                        f"'{resource_to_node[resource].name}' "
                        f"both output to resource {resource!r}. "
                        f"Nodes cannot output to the same resource."
                    )
                resource_to_node[resource] = node
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


@dataclass(frozen=True, repr=False)
class NodeIOGraph(Graph[Node | AnyIO]):
    """Graph with views, nodes and IOs."""

    input_to_nodes: dict[AnyIO, OrderedSet[Node]]
    node_to_outputs: dict[Node, OrderedSet[AnyIO]]
    ios: OrderedSet[AnyIO]
    nodes: OrderedSet[Node]

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


class NamedNodeIOGraph(NodeIOGraph):
    names: dict[Node | AnyIO, str]

    @cached_property
    def names(self) -> dict[Node | AnyIO, str]:
        return {
            **{io: f"io-{idx}" for idx, io in enumerate(self.ios)},
            **{node: node.name for node in self.nodes},
        }

    def __repr__(self):
        lines: list[str] = []

        for io, nodes in self.input_to_nodes.items():
            lines.extend(
                f"{self.names[io]} --> "
                f"{type(node).__name__}:{self.names[node]}"
                for node in nodes
            )

        for node, ios in self.node_to_outputs.items():
            lines.extend(
                f"{type(node).__name__}:{self.names[node]} --> "
                f"{self.names[io]}"
                for io in ios
            )

        return "\n".join(lines)


@dataclass(frozen=True)
class NodeGraph(Graph[Node]):
    """Graph where the edges are node -> [node]."""

    edges: dict[Node, OrderedSet[Node]]
    nodes: OrderedSet[Node]

    @classmethod
    def from_nodes(cls, nodes: set[Node]) -> Self:
        return cls.from_graph(NodeIOGraph.from_nodes(nodes))

    @classmethod
    def from_graph(cls, graph: NodeIOGraph) -> Self:
        edges: dict[Node, OrderedSet[Node]] = defaultdict(OrderedSet)

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


class NamedNodeGraph(NodeGraph):
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
