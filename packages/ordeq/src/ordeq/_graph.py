from collections import defaultdict
from dataclasses import dataclass
from functools import cached_property
from graphlib import TopologicalSorter
from itertools import chain
from typing import Generic, TypeVar, cast

from ordeq._io import IO, AnyIO, Input
from ordeq._nodes import Node, View
from ordeq._patch import _patch_nodes
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
        return tuple(chain.from_iterable(self.topological_levels))

    @cached_property
    def topological_levels(self) -> tuple[tuple[T, ...], ...]:
        levels: list[tuple[T, ...]] = []
        sorter = TopologicalSorter(self.edges)

        sorter.prepare()
        while sorter.is_active():
            level = sorter.get_ready()
            levels.append(tuple(reversed(level)))
            sorter.done(*level)
        return tuple(reversed(levels))


@dataclass(frozen=True)
class NodeResourceGraph(Graph[Resource | Node]):
    edges: dict[Resource | Node, list[Resource | Node]]
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

        # Patching should not be done during graph creation, as it can change
        # the graph topology.
        # TODO: Move the patching to before (for views) and after (for save
        #  and user patches) the graph creation.
        patched_nodes = _patch_nodes(*all_nodes, patches=patches)  # type: ignore[arg-type]

        edges: dict[Resource | Node, list[Resource | Node]] = {
            node: [] for node in patched_nodes
        }
        resources: set[Resource] = set()
        resource_to_node: dict[Resource, Node] = {}

        for node in patched_nodes:
            for ip in node.inputs:
                # Add this point we have converted all view inputs to their
                # sentinel IO, so it's safe to cast input to AnyIO.
                ip_ = cast("AnyIO", ip)

                resource = Resource(ip_._resource)  # noqa: SLF001 (private-member-access)
                resources.add(resource)
                if resource not in edges:
                    edges[resource] = []
                edges[resource].append(node)

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
                edges[node].append(resource)

                if resource not in edges:
                    edges[resource] = []

        return cls(
            edges=edges,
            nodes=set(patched_nodes),
            resources=resources,
        )


@dataclass(frozen=True)
class NodeGraph(Graph[Node]):
    edges: dict[Node, list[Node]]

    @classmethod
    def from_nodes(
        cls,
        nodes: list[Node],
        patches: dict[AnyIO | View, AnyIO] | None = None,
    ) -> Self:
        return cls.from_graph(NodeResourceGraph.from_nodes(nodes, patches))

    @classmethod
    def from_graph(cls, base: NodeResourceGraph) -> Self:
        edges: dict[Node, list[Node]] = {
            cast("Node", node): []
            for node in base.topological_ordering
            if node in base.nodes
        }
        for source in base.topological_ordering:
            if source in base.resources:
                continue
            for target in base.edges[source]:
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


@dataclass(frozen=True)
class NodeIOGraph(Graph[int | Node]):
    # We cannot rely on the __hash__ and __eq__ of IO objects, as they may be
    # overridden by the user. Therefore, this graph maintain strong references
    # to the IO objects.
    # TODO: Clear the references when they are no longer needed.
    edges: dict[int | Node, list[int | Node]]
    ios: dict[int, AnyIO]
    nodes: set[Node]

    @classmethod
    def from_nodes(
        cls,
        nodes: list[Node],
        patches: dict[AnyIO | View, AnyIO] | None = None,
    ) -> Self:
        return cls.from_graph(NodeGraph.from_nodes(nodes, patches))

    @classmethod
    def from_graph(cls, base: NodeGraph) -> Self:
        edges: dict[int | Node, list[int | Node]] = defaultdict(list)
        nodes: set[Node] = set()
        ios: dict[int, AnyIO] = {}
        for node in base.topological_ordering:
            nodes.add(node)
            for input_ in node.inputs:
                input_id = id(input_)
                ios[input_id] = cast("Input | IO", input_)
                edges[input_id].append(node)
            for output in node.outputs:
                output_id = id(output)
                ios[output_id] = output
                edges[node].append(output_id)
        return cls(edges=edges, ios=ios, nodes=nodes)

    def __repr__(self) -> str:
        # Hacky way to generate a deterministic repr of this class.
        # This should move to a separate named graph class.
        lines: list[str] = []
        names: dict[int | Node, str] = {
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
