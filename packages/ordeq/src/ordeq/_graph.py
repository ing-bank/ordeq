from collections import defaultdict
from collections.abc import Sequence
from dataclasses import dataclass
from functools import cached_property
from graphlib import TopologicalSorter
from itertools import chain
from typing import Generic, TypeVar, cast

from ordeq._io import AnyIO, _is_io
from ordeq._nodes import Node, _is_view
from ordeq._resource import Resource

try:
    from typing import Self  # type: ignore[attr-defined]
except ImportError:
    from typing_extensions import Self

T = TypeVar("T")


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

    @cached_property
    def vertices(self) -> set[T]:
        return set(self.edges.keys())

    @cached_property
    def sinks(self) -> set[T]:
        """Finds the sink vertices, i.e., those without successors.

        Returns:
            set of the sink vertices
        """
        return {v for v, targets in self.edges.items() if len(targets) == 0}

    @cached_property
    def sources(self) -> set[T]:
        """Finds the source vertices, i.e., those without predecessors.

        Returns:
            set of the source vertices
        """
        all_targets = {
            target for targets in self.edges.values() for target in targets
        }
        return {v for v in self.edges if v not in all_targets}


@dataclass(frozen=True)
class NodeResourceGraph(Graph[Resource | Node]):
    edges: dict[Resource | Node, list[Resource | Node]]

    @classmethod
    def from_nodes(cls, nodes: Sequence[Node]) -> Self:
        edges: dict[Resource | Node, list[Resource | Node]] = {
            node: [] for node in nodes
        }
        resource_to_node: dict[Resource, Node] = {}

        # if node.checks contains an resource, then this node precedes node(s)
        # with that input that do not have it as a check.
        # add edges from check resource to node(s) with that input
        checks: dict[Resource, list[Resource]] = defaultdict(list)
        for node in nodes:
            for check in node.checks:
                if _is_view(check):
                    resource = Resource(check.outputs[0]._resource)
                elif _is_io(check):
                    resource = Resource(check._resource)
                else:
                    resource = Resource(check)

                for output in node.outputs:
                    checks[resource].append(Resource(output._resource))

        for node in nodes:
            for ip in node.inputs:
                resource = Resource(ip._resource)
                if resource not in edges:
                    edges[resource] = []

                # link checks
                if resource in checks and node.checks == ():
                    for check_resource in checks[resource]:
                        if check_resource not in edges:
                            edges[check_resource] = []

                        edges[check_resource].append(node)

                edges[resource].append(node)

            for op in node.outputs:
                resource = Resource(op._resource)
                if resource in resource_to_node:
                    msg = (
                        f"Nodes '{node.ref}' and "
                        f"'{resource_to_node[resource].ref}' "
                        f"both output to {resource!r}. "
                        f"Nodes cannot output to the same resource."
                    )
                    raise ValueError(msg)

                resource_to_node[resource] = node
                edges[node].append(resource)

                if resource not in edges:
                    edges[resource] = []

        return cls(edges=edges)

    @cached_property
    def nodes(self) -> set[Node]:
        return {node for node in self.edges if isinstance(node, Node)}

    @cached_property
    def resources(self) -> set[Resource]:
        return {
            resource
            for resource in self.edges
            if isinstance(resource, Resource)
        }


@dataclass(frozen=True)
class NodeGraph(Graph[Node]):
    edges: dict[Node, list[Node]]

    @classmethod
    def from_nodes(cls, nodes: Sequence[Node]) -> Self:
        return cls.from_graph(NodeResourceGraph.from_nodes(nodes))

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

    @cached_property
    def nodes(self) -> set[Node]:
        return self.vertices

    # TODO: remove and replace with `viz` method
    def __repr__(self) -> str:
        lines: list[str] = []
        for node in self.topological_ordering:
            if self.edges[node]:
                lines.extend(
                    f"{node.type_name}:{node.ref} --> "
                    f"{next_node.type_name}:{node.ref}"
                    for next_node in self.edges[node]
                )
            else:
                lines.append(f"{node.type_name}:{node.ref}")
        return "\n".join(lines)


# TODO: remove entire class
@dataclass(frozen=True)
class NodeIOGraph(Graph[AnyIO | Node]):
    edges: dict[AnyIO | Node, list[AnyIO | Node]]
    ios: dict[AnyIO, AnyIO]

    @classmethod
    def from_nodes(cls, nodes: Sequence[Node]) -> Self:
        return cls.from_graph(NodeGraph.from_nodes(nodes))

    @classmethod
    def from_graph(cls, base: NodeGraph) -> Self:
        edges: dict[AnyIO | Node, list[AnyIO | Node]] = defaultdict(list)
        ios: dict[AnyIO, AnyIO] = {}
        for node in base.topological_ordering:
            for input_ in node.inputs:
                ios[input_] = input_
                edges[input_].append(node)
            for output in node.outputs:
                ios[output] = output
                edges[node].append(output)
        return cls(edges=edges, ios=ios)

    @cached_property
    def nodes(self) -> set[Node]:
        return {node for node in self.edges if isinstance(node, Node)}

    def __repr__(self) -> str:
        # Hacky way to generate a deterministic repr of this class.
        # This should move to a separate named graph class.
        lines: list[str] = []
        names: dict[AnyIO | Node, str] = {
            **{node: f"{node.type_name}:{node.ref}" for node in self.nodes},
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
