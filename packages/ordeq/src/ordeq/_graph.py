from collections import defaultdict
from dataclasses import dataclass
from functools import cached_property
from graphlib import TopologicalSorter
from typing import Any, Generic, TypeAlias, TypeVar, cast

from ordeq._io import AnyIO
from ordeq._nodes import Node, View

try:
    from typing import Self  # type: ignore[attr-defined]
except ImportError:
    from typing_extensions import Self

NodeIOEdge: TypeAlias = dict[
    Node | View | None, dict[AnyIO, list[Node | View]]
]

T = TypeVar("T")


def _collect_views(*nodes: Node) -> list[Node]:
    all_nodes: dict[Node, None] = {}

    def _collect(*nodes_: Node) -> None:
        for node in nodes_:
            all_nodes[node] = None
            for view in node.views:
                _collect(view)

    _collect(*nodes)
    return list(all_nodes.keys())


class Graph(Generic[T]):
    edges: dict[T, list[T]]

    @cached_property
    def topological_ordering(self) -> tuple[T, ...]:
        return tuple(
            reversed(tuple(TopologicalSorter(self.edges).static_order()))
        )


@dataclass(frozen=True)
class ProjectGraph(Graph[Any]):
    edges: dict[Any, list[Any]]
    ios: set[AnyIO]
    nodes: set[Node]
    views: set[View]

    @classmethod
    def from_nodes(
        cls, nodes: list[Node], patches: dict[AnyIO | View, AnyIO]
    ) -> Self:
        # First pass: collect all views
        all_nodes = _collect_views(*nodes)
        views = [view for view in all_nodes if isinstance(view, View)]

        if patches is None:
            patches = {}
        for view in views:
            patches[view] = view.outputs[0]

        if patches:
            all_nodes = [node._patch_io(patches) for node in all_nodes]  # noqa: SLF001 (private access)

        ios: set[AnyIO] = set()
        edges: dict[Any, list[Any]] = defaultdict(list)

        # Traverse the nodes, sorted by name to preserve determinism:
        for node in all_nodes:
            for ip in node.inputs:
                # Add this point we have converted all view inputs to their
                # sentinel IO, so it's safe to cast input to AnyIO.
                ip_ = cast("AnyIO", ip)

                ios.add(ip_)
                edges[ip_].append(node)
            for op in node.outputs:
                # Add this point we have converted all view inputs to their
                # sentinel IO, so it's safe to cast input to AnyIO.
                op_ = cast("AnyIO", op)

                ios.add(op_)
                edges[node].append(op_)

        return cls(
            edges=edges, ios=ios, nodes=set(all_nodes), views=set(views)
        )


@dataclass(frozen=True)
class NodeIOGraph(Graph[AnyIO | Node]):
    edges: dict[AnyIO | Node, list[AnyIO | Node]]
    ios: set[AnyIO]
    nodes: set[Node]

    @classmethod
    def from_nodes(
        cls,
        nodes: list[Node],
        patches: dict[AnyIO | View, AnyIO] | None = None,
    ) -> Self:
        return cls.from_graph(ProjectGraph.from_nodes(nodes, patches))

    @classmethod
    def from_graph(cls, base: ProjectGraph) -> Self:
        return cls(edges=base.edges, ios=base.ios, nodes=base.nodes)


@dataclass(frozen=True)
class NodeGraph(Graph[Node]):
    edges: dict[Node, list[Node]]
    nodes: set[Node]

    @classmethod
    def from_nodes(cls, nodes: list[Node]) -> Self:
        return cls.from_graph(NodeIOGraph.from_nodes(nodes))

    @classmethod
    def from_graph(cls, base: NodeIOGraph) -> Self:
        edges: dict[AnyIO | Node, list[AnyIO | Node]] = {}
        for source, targets in base.edges.items():
            for target in targets:
                if source in base.ios:
                    edges[target] = base.edges[target]
                elif target in base.ios:
                    continue
                else:
                    edges[source].append(target)
        return cls(edges=edges, nodes=base.nodes)

    @property
    def sink_nodes(self) -> set[Node]:
        """Finds the sink nodes, i.e., nodes without successors.

        Returns:
            set of the sink nodes
        """
        return {s for s, targets in self.edges.items() if len(targets) == 0}
