from collections import defaultdict
from dataclasses import dataclass
from functools import cached_property
from graphlib import TopologicalSorter
from typing import Any, Generic, TypeAlias, TypeVar, cast

from ordeq._io import IO, AnyIO, Input, get_resource, has_resource
from ordeq._nodes import Node, View

try:
    from typing import Self  # type: ignore[attr-defined]
except ImportError:
    from typing_extensions import Self

T = TypeVar("T")

OrderedSet: TypeAlias = dict[T, None]


def add(data: OrderedSet[T], item: T) -> None:
    data[item] = None


def _collect_views(*nodes: Node) -> OrderedSet[View]:
    views: OrderedSet[View] = OrderedSet()

    def _collect(n: Node) -> None:
        for view in n.views:
            if view not in views:
                add(views, view)
            _collect(view)

    for node in nodes:
        _collect(node)
    return views


Tvertex = TypeVar("Tvertex")


class Graph(Generic[Tvertex]):
    edges: dict[Tvertex, OrderedSet[Tvertex]]
    vertices: OrderedSet[Tvertex]

    @cached_property
    def topological_ordering(self) -> tuple[Tvertex, ...]:
        # Adds a fake edge between an artificial start vertex
        # (None) and vertices without an edge:
        edges: dict[Tvertex | None, OrderedSet[Tvertex]] = {
            None: self.vertices,
            **self.edges,
        }
        return cast(
            "tuple[Tvertex]",
            tuple(reversed(tuple(TopologicalSorter(edges).static_order())))[
                1:
            ],
        )

    @cached_property
    def sink_nodes(self) -> set[Tvertex]:
        """Finds the sink nodes, i.e., nodes without successors.

        Returns:
            set of the sink nodes
        """
        return {v for v in self.vertices if v not in self.edges}


@dataclass(kw_only=True)
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
            cls, *nodes: Node, patches: dict[AnyIO | View, AnyIO] | None = None
    ) -> Self:
        # First pass: collect all views
        views = _collect_views(*nodes)
        all_nodes = nodes + tuple(view for view in views)

        if patches is None:
            patches = {}
        for view in views:
            patches[view] = view.outputs[0]

        if patches:
            all_nodes = [node._patch_io(patches) for node in all_nodes]  # noqa: SLF001 (private access)

        resources: OrderedSet[Any] = OrderedSet()
        ios: OrderedSet[AnyIO] = OrderedSet()
        nodes_: OrderedSet[Node] = OrderedSet()

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
        for node in all_nodes:
            add(nodes_, node)
            for ip in node.inputs:
                # At this point we have patched all view inputs with
                # sentinel IOs, so this case is safe:
                ip_ = cast("Input | IO", ip)

                resource = get_resource(ip_)
                add(resources, resource)
                add(resource_to_inputs[resource], ip_)
                add(ios, ip_)
                add(input_to_nodes[ip_], node)
            for op in node.outputs:
                resource = get_resource(op)
                add(resources, resource)
                add(output_to_resources[op], resource)
                if has_resource(op) and resource in resource_to_node:
                    raise ValueError(
                        f"Nodes '{node.name}' and "
                        f"'{resource_to_node[resource].name}' "
                        f"both output to resource {resource!r}. "
                        f"Nodes cannot output to the same resource."
                    )
                resource_to_node[resource] = node
                add(ios, op)
                add(node_to_outputs[node], op)

        return cls(
            resource_to_inputs=resource_to_inputs,
            input_to_nodes=input_to_nodes,
            node_to_outputs=node_to_outputs,
            output_to_resources=output_to_resources,
            resources=resources,
            ios=ios,
            nodes=nodes_,
        )

    @cached_property
    def edges(self) -> dict[Any, Any]:  # type: ignore[override]
        return {
            **self.resource_to_inputs,
            **self.input_to_nodes,
            **self.node_to_outputs,
            **self.output_to_resources,
        }

    @cached_property
    def vertices(self) -> OrderedSet[Any]:  # type: ignore[override]
        return self.resources | self.nodes | self.ios


@dataclass(kw_only=True)
class NodeIOGraph(Graph[Node | AnyIO]):
    """Graph with views, nodes and IOs."""

    input_to_nodes: dict[AnyIO, OrderedSet[Node]]
    node_to_outputs: dict[Node, OrderedSet[AnyIO]]
    ios: OrderedSet[AnyIO]
    nodes: OrderedSet[Node]

    @classmethod
    def from_nodes(
        cls, *nodes: Node, patches: dict[AnyIO | View, AnyIO] | None = None
    ) -> Self:
        return cls.from_graph(BaseGraph.from_nodes(*nodes, patches=patches))

    @classmethod
    def from_graph(cls, graph: BaseGraph):
        return cls(
            input_to_nodes=graph.input_to_nodes,
            node_to_outputs=graph.node_to_outputs,
            ios=graph.ios,
            nodes=graph.nodes,
        )

    @cached_property
    def edges(self) -> dict[AnyIO | Node, OrderedSet[AnyIO | Node]]:  # type: ignore[override]
        return {**self.input_to_nodes, **self.node_to_outputs}

    @cached_property
    def vertices(self) -> OrderedSet[Node | AnyIO]:  # type: ignore[override]
        return self.nodes | self.ios


class NamedNodeIOGraph(NodeIOGraph):
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


@dataclass(frozen=True, kw_only=True)
class NodeGraph(Graph[Node]):
    """Graph where the edges are node -> [node]."""

    edges: dict[Node, OrderedSet[Node]]
    nodes: OrderedSet[Node]

    @classmethod
    def from_nodes(cls, *nodes: Node) -> Self:
        return cls.from_graph(NodeIOGraph.from_nodes(*nodes))

    @classmethod
    def from_graph(cls, graph: NodeIOGraph) -> Self:
        edges: dict[Node, OrderedSet[Node]] = defaultdict(OrderedSet)

        for node, outputs in graph.node_to_outputs.items():
            for output in outputs:
                if output in graph.input_to_nodes:
                    for target in graph.input_to_nodes[output]:
                        add(edges[node], target)
        return cls(edges=edges, nodes=graph.nodes)

    @cached_property
    def vertices(self) -> OrderedSet[Any]:  # type: ignore[override]
        return self.nodes


class NamedNodeGraph(NodeGraph):
    def __repr__(self) -> str:
        lines: list[str] = []
        for source_node, target_nodes in self.edges.items():
            if source_node is None:
                continue
            lines.extend(
                f"{type(source_node).__name__}:{source_node.name} --> "
                f"{type(target_node).__name__}:{target_node.name}"
                for target_node in target_nodes
                if target_node
            )
            if not target_nodes:
                lines.append(
                    f"{type(source_node).__name__}:{source_node.name}"
                )
        return "\n".join(lines)
