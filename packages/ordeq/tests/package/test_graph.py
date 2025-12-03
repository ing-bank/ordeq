from unittest.mock import Mock

import pytest
from ordeq._graph import NodeGraph
from ordeq._nodes import Node, Stub
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
def test_find_sinks(edges, expected):
    g = NodeGraph(edges=edges)
    assert g.sinks == expected


def test_it_builds_a_graph():
    first = Mock(spec=Node)
    first.views = []
    first.name = "first"
    first.inputs = [A]
    first.outputs = [B]
    first.checks = []

    second = Mock(spec=Node)
    second.views = []
    second.name = "second"
    second.inputs = [B, C]
    second.outputs = [D]
    second.checks = []

    third = Mock(spec=Node)
    third.views = []
    third.name = "third"
    third.inputs = [B, D]
    third.outputs = [F]
    third.checks = []

    g = NodeGraph.from_nodes([third, second, first])
    assert g.edges[first] == [Stub(value=B)]
    assert g.edges[Stub(value=B)] == [third, second]
    assert g.edges[second] == [Stub(value=D)]
    assert g.edges[Stub(value=D)] == [third]
    assert g.edges[third] == [Stub(value=F)]
    assert g.nodes == {first, second, third, Stub(value=A), Stub(value=B), Stub(value=C), Stub(value=D), Stub(value=F)}


def test_it_builds_graph_with_single_node():
    first = Mock(spec=Node)
    first.name = "first"
    first.inputs = [A]
    first.outputs = [B]
    first.views = []
    first.checks = []

    g = NodeGraph.from_nodes([first])
    assert g.edges == {first: [Stub(value=B)], Stub(value=B): [], Stub(value=A): [first]}
    assert set(g.nodes) == {first, Stub(value=A), Stub(value=B)}


def test_it_raises_error_on_duplicated_outputs():
    first = Mock(spec=Node)
    first.views = []
    first.name = "first"
    first.inputs = [A]
    first.outputs = [B]
    first.checks = []

    second = Mock(spec=Node)
    second.views = []
    second.name = "second"
    second.inputs = [D]
    second.outputs = [B]
    second.checks = []

    with pytest.raises(
        ValueError, match=r"Nodes cannot output to the same resource."
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

    g = NodeGraph(edges=edges)
    assert g.topological_ordering == expected
