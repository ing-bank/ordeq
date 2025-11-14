from dataclasses import dataclass
from functools import cached_property
from graphlib import TopologicalSorter
from typing import Generic, TypeVar, cast

from ordeq._io import AnyIO
from ordeq._nodes import Node, View
from ordeq._resource import Resource

try:
    from typing import Self  # type: ignore[attr-defined]
except ImportError:
    from typing_extensions import Self

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
class ProjectGraph(Graph[AnyIO | Node]):
    edges: dict[AnyIO | Node, list[AnyIO | Node]]
    ios: set[AnyIO]
    nodes: set[Node]
    resources: set[Resource]

    @classmethod
    def from_nodes(
        cls,
        nodes: list[Node],
        patches: dict[AnyIO | View, AnyIO] | None = None,
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

        ios_: set[AnyIO] = set()
        edges: dict[AnyIO | Node, list[AnyIO | Node]] = {
            node: [] for node in all_nodes
        }
        resources: set[Resource] = set()
        resource_to_node: dict[Resource, Node] = {}

        for node in all_nodes:
            for ip in node.inputs:
                # Add this point we have converted all view inputs to their
                # sentinel IO, so it's safe to cast input to AnyIO.
                ip_ = cast("AnyIO", ip)

                ios_.add(ip_)

                if ip_ not in edges:
                    edges[ip_] = []
                edges[ip_].append(node)

                resource = Resource(ip_._resource)  # noqa: SLF001 (private-member-access)
                resources.add(resource)

            for op in node.outputs:
                resource = Resource(op._resource)  # noqa: SLF001 (private-member-access)

                if resource in resource_to_node:
                    msg = (
                        f"Nodes '{node.name}' and "
                        f"'{resource_to_node[resource].name}' "
                        f"both output to {resource!r}. "
                        f"Nodes cannot output to the same resource."
                    )
                    raise ValueError(msg)

                resources.add(resource)
                resource_to_node[resource] = node
                ios_.add(op)
                edges[node].append(op)

                if op not in edges:
                    edges[op] = []

        return cls(
            edges=edges, ios=ios_, nodes=set(all_nodes), resources=resources
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

    def __repr__(self) -> str:
        # Hacky way to generate a deterministic repr of this class.
        # This should move to a separate named graph class.
        lines: list[str] = []
        names: dict[Node | AnyIO, str] = {
            **{
                node: f"{type(node).__name__}:{node.name}"
                for node in self.nodes
            },
            **{
                io: f"io-{i}"
                for i, io in enumerate(
                    io for io in self.topological_ordering if io in self.ios
                )
            },
        }

        for vertex in self.topological_ordering:
            lines.extend(
                f"{names[vertex]} --> {names[next_vertex]}"
                for next_vertex in self.edges[vertex]
            )

        return "\n".join(lines)


@dataclass(frozen=True)
class NodeGraph(Graph[Node]):
    edges: dict[Node, list[Node]]

    @classmethod
    def from_nodes(cls, nodes: list[Node]) -> Self:
        return cls.from_graph(NodeIOGraph.from_nodes(nodes))

    @classmethod
    def from_graph(cls, base: NodeIOGraph) -> Self:
        edges: dict[Node, list[Node]] = {
            cast("Node", node): [] for node in base.edges if node in base.nodes
        }
        for source, targets in base.edges.items():
            if source in base.ios:
                continue
            for target in targets:
                if target in base.edges:
                    edges[source].extend(base.edges[target])  # type: ignore[index,arg-type]
        return cls(edges=edges)

    @property
    def sink_nodes(self) -> set[Node]:
        """Finds the sink nodes, i.e., nodes without successors.

        Returns:
            set of the sink nodes
        """
        return {s for s, targets in self.edges.items() if len(targets) == 0}

    @cached_property
    def nodes(self) -> list[Node]:
        return list(self.edges.keys())

    def __repr__(self) -> str:
        lines: list[str] = []
        for node in self.topological_ordering:
            if self.edges[node]:
                lines.extend(
                    f"{type(node).__name__}:{node.name} --> "
                    f"{type(next_node).__name__}:{next_node.name}"
                    for next_node in self.edges[node]
                )
            else:
                lines.append(f"{type(node).__name__}:{node.name}")
        return "\n".join(lines)
