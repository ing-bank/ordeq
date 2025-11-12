from collections import defaultdict
from dataclasses import dataclass
from functools import cached_property
from graphlib import TopologicalSorter
from typing import Any, TypeAlias, TypeVar, cast

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


@dataclass(frozen=True)
class NodeIOGraph:
    edges: dict[AnyIO | Node, list[AnyIO | Node]]
    ios: set[AnyIO]
    nodes: set[Node]

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

        ios: set[AnyIO] = set()
        edges: dict[Any, list[Any]] = defaultdict(list)
        output_to_node: dict[AnyIO, Node | View] = {}

        # Traverse the nodes, sorted by name to preserve determinism:
        for node in all_nodes:
            for ip in node.inputs:
                # Add this point we have converted all view inputs to their
                # sentinel IO, so it's safe to cast input to AnyIO.
                ip_ = cast("AnyIO", ip)

                ios.add(ip_)
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
                ios.add(op)
                edges[node].append(op)

        return cls(edges=dict(edges), ios=ios, nodes=set(all_nodes))


@dataclass(frozen=True)
class NodeGraph:
    edges: dict[Node, list[Node]]
    nodes: set[Node]

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
        return cls(edges=dict(edges), nodes=base.nodes)

    @property
    def sink_nodes(self) -> set[Node]:
        """Finds the sink nodes, i.e., nodes without successors.

        Returns:
            set of the sink nodes
        """
        return {s for s, targets in self.edges.items() if len(targets) == 0}

    @cached_property
    def topological_ordering(self) -> tuple[T, ...]:
        edges = {None: list(self.nodes), **self.edges}
        return tuple(reversed(tuple(TopologicalSorter(edges).static_order())))[
            1:
        ]

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
