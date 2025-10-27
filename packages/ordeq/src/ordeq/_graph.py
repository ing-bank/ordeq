import operator
from collections import defaultdict
from functools import cached_property
from graphlib import TopologicalSorter
from typing import TypeAlias

from ordeq._fqn import FQN, fqn_to_str, str_to_fqn
from ordeq._io import AnyIO
from ordeq._nodes import Node, View

try:
    from typing import Self  # type: ignore[attr-defined]
except ImportError:
    from typing_extensions import Self


NamedNode: TypeAlias = tuple[FQN, Node]
EdgesType: TypeAlias = dict[NamedNode, list[NamedNode]]


def _collect_views(nodes: dict[FQN, Node]) -> dict[FQN, View]:
    """Recursively collects all views from the given nodes.

    Args:
        nodes: set of `Node` objects

    Returns:
        a set of `View` objects
    """

    views: dict[FQN, View] = {}
    for node in nodes.values():
        node_views = {str_to_fqn(view.name): view for view in node.views}
        views |= node_views | _collect_views(node_views)  # type: ignore[arg-type]
    return views


def _build_graph(nodes: dict[FQN, Node]) -> EdgesType:
    """Builds a mapping of node to node(s), i.e., the edge map of a graph.

    Args:
        nodes: iterable of `Node` objects

    Returns:
        a mapping of node to node(s), i.e., the edge map of a graph

    Raises:
        ValueError: if an output is defined by more than one node
    """

    output_to_node: dict[View | AnyIO, tuple[FQN, View | Node]] = {
        view: (str_to_fqn(view.name), view)
        for view in nodes.values()
        if isinstance(view, View)
    }
    input_to_nodes: defaultdict = defaultdict(list)
    edges: EdgesType = {named_node: [] for named_node in nodes.items()}
    for name, node in nodes.items():
        if isinstance(node, Node):
            for output_ in node.outputs:
                if output_ in output_to_node:
                    msg = (
                        f"IO {output_} cannot be outputted "
                        f"by more than one node"
                    )
                    raise ValueError(msg)
                output_to_node[output_] = name, node
        for input_ in node.inputs:
            input_to_nodes[input_].append((name, node))
    for node_output, named_node in output_to_node.items():
        if node_output in input_to_nodes:
            edges[named_node] += input_to_nodes[node_output]
    return edges


def _find_topological_ordering(edges: EdgesType) -> tuple[NamedNode, ...]:
    """Topological sort.

    Args:
        edges: mapping of node to node(s), i.e., the edge map of a graph

    Returns:
            a tuple of nodes in topological order
    """
    return tuple(reversed(tuple(TopologicalSorter(edges).static_order())))


def _find_sink_nodes(edges: EdgesType) -> set[NamedNode]:
    """Finds the sinks nodes, i.e. nodes without successors.

    Args:
        edges: the graph

    Returns:
        set of the sink nodes

    """

    return {s for s, targets in edges.items() if len(targets) == 0}


def _nodes(edges: EdgesType) -> dict[FQN, Node]:
    """Returns the set of all nodes.

    Args:
        edges: the graph

    Returns:
        set of all nodes
    """

    return dict(edges.keys())


class NodeGraph:
    def __init__(self, edges: EdgesType):
        self.edges = edges

    @classmethod
    def from_nodes(cls, nodes: dict[FQN, Node]) -> Self:
        views = _collect_views(nodes)
        return cls(_build_graph(nodes | views))

    @cached_property
    def topological_ordering(self) -> tuple[NamedNode, ...]:
        return _find_topological_ordering(self.sorted_edges)

    @cached_property
    def sorted_edges(self) -> EdgesType:
        return dict(
            sorted(
                [
                    (node, sorted(targets, key=operator.itemgetter(0)))
                    for node, targets in self.edges.items()
                ],
                key=lambda x: x[0][0],
            )
        )

    @property
    def sink_nodes(self) -> set[NamedNode]:
        """Finds the sink nodes, i.e., nodes without successors.

        Returns:
            set of the sink nodes
        """
        return _find_sink_nodes(self.edges)

    @property
    def nodes(self) -> dict[FQN, Node]:
        """Returns the set of all nodes in this graph.

        Returns:
            all nodes in this graph
        """

        return _nodes(self.edges)

    def __repr__(self) -> str:
        lines = ["NodeGraph:", "  Edges:"]
        for (name, _), targets in self.sorted_edges.items():
            targets_str = ", ".join(fqn_to_str(n) for n, _ in targets)
            lines.append(f"     {fqn_to_str(name)} -> [{targets_str}]")
        lines.append("  Nodes:")
        lines.extend(
            f"     {fqn_to_str(name)}: {node!r}"
            for name, node in self.sorted_edges
        )
        return "\n".join(lines)
