from unittest.mock import Mock

import pytest
from ordeq._graph import NodeGraph, _collect_views
from ordeq._nodes import Node
from ordeq_common import StringBuffer

A, B, C, D, E, F = [StringBuffer(c) for c in "ABCDEF"]


@pytest.mark.parametrize(
    ("edges", "expected"),
    [
        ({"A": ["B"], "B": []}, {"B"}),
        ({"A": ["B", "C"], "B": [], "C": [], "D": ["A"]}, {"B", "C"}),
        ({"A": ["B"], "B": ["A"]}, set()),
        ({"A": [], "B": [], "C": []}, {"A", "B", "C"}),
        ({}, set()),
    ],
)
def test_find_sink_nodes(edges, expected):
    g = NodeGraph({})
    g.edges = edges
    assert g.sink_nodes == expected


def test_it_builds_a_graph():
    first = Mock(spec=Node)
    first.views = []
    first.name = "first"
    first.inputs = [A]
    first.outputs = [B]

    second = Mock(spec=Node)
    second.views = []
    second.name = "second"
    second.inputs = [B, C]
    second.outputs = [D]

    third = Mock(spec=Node)
    third.views = []
    third.name = "third"
    third.inputs = [B, D]
    third.outputs = [F]

    g = NodeGraph.from_nodes({third, second, first})
    assert g.edges == {first: [second, third], second: [third], third: []}
    assert g.nodes == {first, second, third}


def test_it_builds_graph_with_single_node():
    first = Mock(spec=Node)
    first.name = "first"
    first.inputs = [A]
    first.outputs = [B]
    first.views = []

    g = NodeGraph.from_nodes({first})
    assert g.edges == {first: []}
    assert g.nodes == {first}


def test_it_raises_error_on_duplicated_outputs():
    first = Mock(spec=Node)
    first.views = []
    first.name = "first"
    first.inputs = [A]
    first.outputs = [B]

    second = Mock(spec=Node)
    second.views = []
    second.name = "second"
    second.inputs = [D]
    second.outputs = [B]

    with pytest.raises(
        ValueError, match="cannot be outputted by more than one node"
    ):
        NodeGraph.from_nodes({first, second})


@pytest.mark.parametrize(
    ("edges", "expected"),
    [
        (
            # Example 0:
            # 0 ---
            # |     |
            # 1 --- 2
            {0: [1, 2], 1: [2], 2: []},
            (0, 1, 2),
        ),
        (
            # Example 1:
            # 0 --- 2
            # |     |
            # 1 --- 3
            {0: [1, 2], 1: [3], 2: [3], 3: []},
            (0, 2, 1, 3),
        ),
        (
            # Example 2:
            # 0 --- 2
            # |
            # 1
            {0: [1, 2], 1: [], 2: []},
            (0, 2, 1),
        ),
        (
            # Example 3:
            # 0 --- 2
            # |  /  |
            # 1 --- 3
            {0: [1, 2], 1: [2, 3], 2: [3], 3: []},
            (0, 1, 2, 3),
        ),
        (
            # Example 4:
            # 0 --- 2
            # |  X  |
            # 1 --- 3
            {0: [1, 2, 3], 1: [2, 3], 2: [3], 3: []},
            (0, 1, 2, 3),
        ),
    ],
)
def test_it_finds_a_topological_ordering(edges, expected):
    # Note that even though for some of the examples there exist
    # multiple valid topological orderings, the ordering is
    # deterministic (as dictionaries are ordered).

    g = NodeGraph({})
    g.edges = edges
    actual = g.topological_ordering
    assert actual == expected


def test_collect_views():
    # Edge case: empty set
    assert _collect_views() == []

    # Node with no views
    node1 = Mock()
    node1.views = []
    assert _collect_views(node1) == []

    # Node with a single view
    view1 = Mock(spec=Node)
    view1.views = []
    node2 = Mock(spec=Node)
    node2.views = [view1]
    assert _collect_views(node2) == [view1]

    # Node with multiple views
    view2 = Mock(spec=Node)
    view2.views = []
    view3 = Mock(spec=Node)
    view3.views = []
    node3 = Mock()
    node3.views = [view2, view3]
    assert _collect_views(node3) == [view2, view3]

    # Nested views: a view that itself has a view
    nested_view = Mock(spec=Node)
    nested_view.views = []
    view4 = Mock(spec=Node)
    view4.views = [nested_view]
    node4 = Mock(spec=Node)
    node4.views = [view4]
    # collect_views should recursively collect nested_view
    assert _collect_views(node4) == [view4, nested_view]

    # Multiple nodes with overlapping views
    node5 = Mock(spec=Node)
    node6 = Mock(spec=Node)
    view1.views = []
    view2.views = []
    view3.views = []
    node5.views = [view1, view2]
    node6.views = [view2, view3]
    assert _collect_views(node5, node6) == [view1, view2, view3]

    # Same example as above but different order of args
    # This shows that the collection is ordered
    node5 = Mock(spec=Node)
    node6 = Mock(spec=Node)
    view1.views = []
    view2.views = []
    view3.views = []
    node5.views = [view1, view2]
    node6.views = [view2, view3]
    assert _collect_views(node6, node5) == [view2, view3, view1]
