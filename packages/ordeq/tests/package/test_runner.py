import copy

from ordeq import node
from ordeq._graph import NodeGraph
from ordeq._nodes import _create_node, get_node
from ordeq._runner import _run_graph, _run_node, run
from ordeq_common import StringBuffer

A, B, D = [StringBuffer(c) for c in "ABD"]
C = StringBuffer()
E = StringBuffer()
F = StringBuffer()


def test_run_regular_node():
    Bp = copy.copy(B)
    Bp.unpersist()
    node = _create_node(inputs=(A,), outputs=(Bp,), func=lambda x: x + x)
    computed = _run_node(node, hooks=())
    assert computed[Bp] == "AA"


def test_run_node_returns_none():
    node = _create_node(inputs=(A,), outputs=(), func=lambda _: None)
    computed = _run_node(node, hooks=())
    assert computed == {}


def test_run_node_with_zero_inputs():
    Bp = copy.copy(B)
    Bp.unpersist()
    node = _create_node(inputs=(), outputs=(Bp,), func=lambda: "something")
    loaded = {Bp: "something"}
    computed = _run_node(node, hooks=())
    assert loaded == computed


def test_run_node_with_zero_inputs_and_outputs():
    node = _create_node(inputs=(), outputs=(), func=lambda: print("Hello!"))
    loaded = {}
    computed = _run_node(node, hooks=())
    assert loaded == computed


def test_run_graph_all():
    plus = node(func=lambda x, y: f"{x} + {y}", inputs=(A, B), outputs=(C,))
    minus = node(func=lambda x, y: f"{x} - {y}", inputs=(C, D), outputs=(E,))
    square = node(func=lambda x: f"({x})^2", inputs=(E,), outputs=(F,))
    nodes = [get_node(plus), get_node(minus), get_node(square)]
    expected_data_store = {
        C: "A + BAAsomething",
        E: "A + BAAsomething - D",
        F: "(A + BAAsomething - D)^2",
    }
    data_store = _run_graph(NodeGraph.from_nodes(nodes))
    assert data_store == expected_data_store


def test_run_graph_two():
    plus = node(func=lambda x, y: f"{x} + {y}", inputs=(A, B), outputs=(C,))
    minus = node(func=lambda x, y: f"{x} - {y}", inputs=(C, D), outputs=(E,))
    nodes = [get_node(plus), get_node(minus)]
    expected_data_store = {C: "A + BAAsomething", E: "A + BAAsomething - D"}
    data_store = _run_graph(NodeGraph.from_nodes(nodes))
    assert data_store == expected_data_store


def test_run_graph_one():
    plus = node(func=lambda x, y: f"{x} + {y}", inputs=(A, B), outputs=(C,))
    nodes = [get_node(plus)]
    expected_data_store = {C: "A + BAAsomething"}
    data_store = _run_graph(NodeGraph.from_nodes(nodes))
    assert data_store == expected_data_store


def test_run_parametrized_all():
    plus = node(func=lambda x, y: f"{x} + {y}", inputs=(A, B), outputs=(C,))
    minus = node(func=lambda x, y: f"{x} - {y}", inputs=(C, D), outputs=(E,))
    square = node(func=lambda x: f"({x})^2", inputs=(E,), outputs=(F,))
    data_store = run(plus, minus, square)
    expected_data_store = {
        C: "A + BAAsomething",
        E: "A + BAAsomething - D",
        F: "(A + BAAsomething - D)^2",
    }
    assert data_store == expected_data_store


def test_run_parametrized_two():
    plus = node(func=lambda x, y: f"{x} + {y}", inputs=(A, B), outputs=(C,))
    minus = node(func=lambda x, y: f"{x} - {y}", inputs=(C, D), outputs=(E,))
    data_store = run(plus, minus)
    expected_data_store = {C: "A + BAAsomething", E: "A + BAAsomething - D"}
    assert data_store == expected_data_store


def test_run_parametrized_one():
    plus = node(func=lambda x, y: f"{x} + {y}", inputs=(A, B), outputs=(C,))
    data_store = run(plus)
    expected_data_store = {C: "A + BAAsomething"}
    assert data_store == expected_data_store
