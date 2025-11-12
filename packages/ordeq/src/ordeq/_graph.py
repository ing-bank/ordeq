from collections import defaultdict
from dataclasses import dataclass
from functools import cached_property
from graphlib import TopologicalSorter
from typing import Any, TypeVar, cast

from ordeq._io import AnyIO
from ordeq._nodes import Node, View

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


@dataclass(frozen=True)
class NodeIOGraph:
    edges: dict[AnyIO | Node, list[AnyIO | Node]]
    ios: list[AnyIO]
    nodes: list[Node]

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

        ios: list[AnyIO] = []
        edges: dict[Any, list[Any]] = defaultdict(list)
        output_to_node: dict[AnyIO, Node | View] = {}

        for node in all_nodes:
            for ip in node.inputs:
                # Add this point we have converted all view inputs to their
                # sentinel IO, so it's safe to cast input to AnyIO.
                ip_ = cast("AnyIO", ip)

                ios.append(ip_)
                edges[ip_].append(node)
            for op in node.outputs:
                if op in output_to_node:
                    msg = (
                        f"IO {op} cannot be outputted by "
                        f"more than one node ({output_to_node[op].name} "
                        f"and {node.name})"
                    )
                    raise ValueError(msg)

                output_to_node[op] = node
                ios.append(op)
                edges[node].append(op)

        return cls(edges=dict(edges), ios=ios, nodes=all_nodes)

    @cached_property
    def topological_ordering(self) -> tuple[Node | AnyIO, ...]:
        # Adds an edge between a dummy vertex all unconnected nodes:
        edges: dict[int | AnyIO | Node, list[AnyIO | Node]] = {
            0: [*self.nodes, *self.ios],
            **self.edges,  # type: ignore[dict-item]
        }
        ordering = tuple(
            reversed(tuple(TopologicalSorter(edges).static_order()))
        )
        # The dummy vertex is at index 0:
        return cast("tuple[Node, ...]", ordering[1:])

    def __repr__(self) -> str:
        # Hacky way to generate a deterministic repr of this class.
        # This should move to a separate named graph class.
        lines: list[str] = []
        names: dict[Node | AnyIO, str] = {
            **{
                node: f"{type(node).__name__}:{node.name}"
                for node in self.nodes
            },
            **{io: f"io-{i}" for i, io in enumerate(self.ios)},
        }

        for vertex in self.edges:
            lines.extend(
                f"{names[vertex]} --> {names[next_vertex]}"
                for next_vertex in self.edges[vertex]
            )

        return "\n".join(lines)


@dataclass(frozen=True)
class NodeGraph:
    edges: dict[Node, list[Node]]
    nodes: list[Node]

    @classmethod
    def from_nodes(cls, nodes: list[Node]) -> Self:
        return cls.from_graph(NodeIOGraph.from_nodes(nodes))

    @classmethod
    def from_graph(cls, base: NodeIOGraph) -> Self:
        edges: dict[AnyIO | Node, list[AnyIO | Node]] = defaultdict(list)
        for source, targets in base.edges.items():
            if source in base.ios:
                continue
            for target in targets:
                if target in base.edges:
                    edges[source].extend(base.edges[target])
        return cls(
            edges=dict(edges),  # type: ignore[arg-type]
            nodes=base.nodes,
        )

    @property
    def sink_nodes(self) -> set[Node]:
        """Finds the sink nodes, i.e., nodes without successors.

        Returns:
            set of the sink nodes
        """
        return {s for s, targets in self.edges.items() if len(targets) == 0}

    @cached_property
    def topological_ordering(self) -> tuple[Node, ...]:
        # Adds an edge between a dummy vertex all unconnected nodes:
        edges: dict[Node | None, list[Node]] = {
            None: self.nodes,
            **self.edges,  # type: ignore[dict-item]
        }
        ordering = tuple(
            reversed(tuple(TopologicalSorter(edges).static_order()))
        )
        # The dummy vertex is at index 0:
        return cast("tuple[Node, ...]", ordering[1:])

    def __repr__(self) -> str:
        lines: list[str] = []
        for node in self.topological_ordering:
            if node in self.edges:
                lines.extend(
                    f"{type(node).__name__}:{node.name} --> "
                    f"{type(next_node).__name__}:{next_node.name}"
                    for next_node in self.edges[node]
                )
            else:
                lines.append(f"{type(node).__name__}:{node.name}")
        return "\n".join(lines)
