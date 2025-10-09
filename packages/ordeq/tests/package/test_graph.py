from unittest.mock import Mock

import pytest
from ordeq._graph import (
    _build_graph,
    _find_sink_nodes,
    _find_topological_ordering,
    _nodes,
)
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
    assert _find_sink_nodes(edges) == expected


def test_it_builds_a_graph():
    first = Mock()
    first.name = "first"
    first.inputs = [A]
    first.outputs = [B]

    second = Mock()
    second.name = "second"
    second.inputs = [B, C]
    second.outputs = [D]

    third = Mock()
    third.name = "third"
    third.inputs = [B, D]
    third.outputs = [F]

    edges = _build_graph([third, second, first])
    assert edges == {first: [third, second], second: [third], third: []}
    assert _nodes(edges) == {first, second, third}


def test_it_builds_graph_with_single_node():
    first = Mock()
    first.name = "first"
    first.inputs = [A]
    first.outputs = [B]

    edges = _build_graph([first])
    assert edges == {first: []}
    assert _nodes(edges) == {first}


def test_it_raises_error_on_duplicated_outputs():
    first = Mock()
    first.name = "first"
    first.inputs = [A]
    first.outputs = [B]

    second = Mock()
    second.name = "second"
    second.inputs = [D]
    second.outputs = [B]

    with pytest.raises(
        ValueError, match="cannot be outputted by more than one node"
    ):
        _build_graph([first, second])


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

    actual = _find_topological_ordering(edges)
    assert actual == expected
