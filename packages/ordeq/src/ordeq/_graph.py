from collections import defaultdict
from functools import cached_property
from graphlib import TopologicalSorter
from typing import TypeAlias

from ordeq._io import AnyIO
from ordeq._nodes import Node, View

try:
    from typing import Self  # type: ignore[attr-defined]
except ImportError:
    from typing_extensions import Self


NodeIOEdge: TypeAlias = dict[
    Node | View | None, dict[AnyIO, list[Node | View]]
]


def _collect_views(nodes_: set[Node]) -> set[View]:
    views: set[View] = set()
    for node in nodes_:
        node_views = set(node.views)
        views |= node_views | _collect_views(node_views)  # type: ignore[arg-type]
    return views


class NodeIOGraph:
    """Graph with views, nodes and IOs."""

    def __init__(self, edges: NodeIOEdge):
        self.edges = edges

    @classmethod
    def from_nodes(
        cls, nodes: set[Node], patches: dict[AnyIO | View, AnyIO] | None = None
    ) -> Self:
        edges: NodeIOEdge = defaultdict(dict)

        # First pass: collect all views
        views = _collect_views(nodes)
        all_nodes = nodes | views

        if patches is None:
            patches = {}
        for view in sorted(views, key=lambda n: n.name):
            patches[view] = view.outputs[0]

        if patches:
            all_nodes = {node._patch_io(patches) for node in all_nodes}  # noqa: SLF001 (private access)

        # Second pass: register outputs
        output_to_node: dict[AnyIO, Node | View] = {}
        for node in sorted(all_nodes, key=lambda n: n.name):
            for output in node.outputs:
                if output in output_to_node:
                    msg = (
                        f"IO {output} cannot be outputted by "
                        f"more than one node ({output_to_node[output].name} "
                        f"and {node.name})"
                    )
                    raise ValueError(msg)
                output_to_node[output] = node
                edges[node][output] = []

        # Third pass: connect nodes through inputs
        for node in sorted(all_nodes, key=lambda n: n.name):
            for input_ in node.inputs:
                if input_ in output_to_node:
                    source_node = output_to_node[input_]  # type: ignore[index]
                    edges[source_node][input_].append(node)  # type: ignore[index]
                else:
                    edges[None].setdefault(input_, []).append(node)  # type: ignore[arg-type]

        return cls(dict(edges))

    @property
    def ios(self) -> set[AnyIO]:
        ios: set[AnyIO] = set()
        for targets in self.edges.values():
            ios.update(targets.keys())
        return ios

    def __repr__(self) -> str:
        lines: list[str] = []

        io_ids: dict[AnyIO, str] = {}
        for source_node, targets in self.edges.items():
            for io, target_nodes in sorted(
                targets.items(),
                key=lambda item: tuple(sorted(n.name for n in item[1])),
            ):
                if io not in io_ids:
                    io_ids[io] = f"io-{len(io_ids) + 1}"
                io_id = io_ids[io]

                if source_node is not None:
                    lines.append(
                        f"{type(source_node).__name__}:{source_node.name} --> "
                        f"{io_id}"
                    )

                lines.extend(
                    f"{io_id} --> "
                    f"{type(target_node).__name__}:{target_node.name}"
                    for target_node in target_nodes
                )

        return "\n".join(lines)


NodeEdge: TypeAlias = dict[Node, list[Node]]


class NodeGraph:
    """Graph where the edges are node -> [node]."""

    def __init__(self, edges: NodeEdge):
        self.edges = {
            node: sorted(targets, key=lambda n: n.name)
            for node, targets in sorted(edges.items(), key=lambda n: n[0].name)
        }

    @classmethod
    def from_nodes(cls, nodes: set[Node]) -> Self:
        return cls.from_graph(NodeIOGraph.from_nodes(nodes))

    @classmethod
    def from_graph(cls, graph: NodeIOGraph) -> Self:
        edges: dict[Node, list[Node]] = {}

        for source_node, io_dict in graph.edges.items():
            if source_node is None:
                continue
            edges[source_node] = []
            for target_nodes in io_dict.values():
                for target_node in target_nodes:
                    edges[source_node].append(target_node)

        return cls(edges)

    @property
    def sink_nodes(self) -> set[Node]:
        """Finds the sink nodes, i.e., nodes without successors.

        Returns:
            set of the sink nodes
        """
        return {s for s, targets in self.edges.items() if len(targets) == 0}

    @property
    def nodes(self) -> set[Node]:
        return set(self.edges.keys()) | {
            node for targets in self.edges.values() for node in targets
        }

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
