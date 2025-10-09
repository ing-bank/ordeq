from collections.abc import Iterable
from graphlib import TopologicalSorter

from ordeq._nodes import Node

try:
    from typing import Self  # type: ignore[attr-defined]
except ImportError:
    from typing_extensions import Self
EdgesType = dict[Node, list[Node]]


def _build_graph(nodes: Iterable[Node]) -> EdgesType:
    """Builds a mapping of node to node(s), i.e., the edge map of a graph.

    Args:
        nodes: iterable of `Node` objects

    Returns:
        a mapping of node to node(s), i.e., the edge map of a graph

    Raises:
        ValueError: if an output is defined by more than one node
    """
    output_to_node: dict = {}
    input_to_nodes: dict = {}
    edges: dict = {node: [] for node in nodes}
    for node in nodes:
        for output_ in node.outputs:
            if output_ in output_to_node:
                msg = f"IO {output_} cannot be outputted by more than one node"
                raise ValueError(msg)
            output_to_node[output_] = node
        for input_ in node.inputs:
            input_to_nodes[input_] = [*input_to_nodes.get(input_, []), node]
    for node_output, node in output_to_node.items():
        if node_output in input_to_nodes:
            edges[node] += input_to_nodes[node_output]
    return edges


def _find_topological_ordering(edges: EdgesType) -> tuple[Node, ...]:
    """Topological sort.

    Args:
        edges: mapping of node to node(s), i.e., the edge map of a graph

    Returns:
            a tuple of nodes in topological order
    """
    return tuple(reversed(tuple(TopologicalSorter(edges).static_order())))


def _find_sink_nodes(edges: EdgesType) -> set[Node]:
    """Finds the sinks nodes, i.e. nodes without successors.

    Args:
        edges: the graph

    Returns:
        set of the sink nodes

    """

    return {s for s, targets in edges.items() if len(targets) == 0}


def _nodes(edges: EdgesType) -> set[Node]:
    """Returns the set of all nodes.

    Args:
        edges: the graph

    Returns:
        set of all nodes
    """

    return set(edges.keys())


class NodeGraph:
    def __init__(self, edges: EdgesType):
        self.edges = edges

    @classmethod
    def from_nodes(cls, nodes: Iterable[Node]) -> Self:
        return cls(_build_graph(nodes))

    @property
    def topological_ordering(self) -> tuple[Node, ...]:
        return _find_topological_ordering(self.sorted_edges)

    @property
    def sorted_edges(self) -> EdgesType:
        return dict(
            sorted(
                [
                    (node, sorted(targets, key=lambda n: n.name))
                    for node, targets in self.edges.items()
                ],
                key=lambda x: x[0].name,
            )
        )

    @property
    def sink_nodes(self) -> set[Node]:
        """Finds the sink nodes, i.e., nodes without successors.

        Returns:
            set of the sink nodes
        """
        return _find_sink_nodes(self.edges)

    @property
    def nodes(self) -> set[Node]:
        """Returns the set of all nodes in this graph.

        Returns:
            all nodes in this graph
        """

        return _nodes(self.edges)

    def __repr__(self) -> str:
        lines = ["NodeGraph:", "  Edges:"]
        for node, targets in self.sorted_edges.items():
            targets_str = ", ".join(t.name for t in targets)
            lines.append(f"     {node.name} -> [{targets_str}]")
        lines.append("  Nodes:")
        lines.extend(f"     {node!r}" for node in self.sorted_edges)
        return "\n".join(lines)
