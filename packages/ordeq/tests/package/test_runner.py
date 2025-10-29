from ordeq import node
from ordeq._graph import NodeGraph
from ordeq._nodes import create_node, get_node
from ordeq._runner import _run_graph, _run_node, run
from ordeq_common import StringBuffer


def test_run_regular_node():
    a = StringBuffer("a")
    b = StringBuffer("b")
    node = create_node(inputs=(a,), outputs=(b,), func=lambda x: x + x)
    _run_node(node, hooks=())
    assert b.load() == "aa"


def test_run_node_with_zero_inputs():
    b = StringBuffer("b")
    node = create_node(inputs=(), outputs=(b,), func=lambda: "something")
    _run_node(node, hooks=())
    assert b.load() == "something"


def test_run_graph_all():
    a, b, c, d, e, f = [StringBuffer(x) for x in "abcdef"]

    plus = node(func=lambda x, y: f"({x} + {y})", inputs=(a, b), outputs=(c,))
    minus = node(func=lambda x, y: f"({x} - {y})", inputs=(c, d), outputs=(e,))
    square = node(func=lambda x: f"({x})^2", inputs=(e,), outputs=(f,))

    nodes = [get_node(plus), get_node(minus), get_node(square)]
    _run_graph(NodeGraph.from_nodes(nodes))
    assert c.load() == "c(a + b)"
    assert e.load() == "e((a + b) - d)"
    assert f.load() == "f(((a + b) - d))^2"


def test_run_graph_two():
    a, b, c, d, e = [StringBuffer(x) for x in "abcde"]
    plus = node(func=lambda x, y: f"({x} + {y})", inputs=(a, b), outputs=(c,))
    minus = node(func=lambda x, y: f"({x} - {y})", inputs=(c, d), outputs=(e,))
    nodes = [get_node(plus), get_node(minus)]
    _run_graph(NodeGraph.from_nodes(nodes))
    assert c.load() == "c(a + b)"
    assert e.load() == "e((a + b) - d)"


def test_run_graph_one():
    a, b, c = [StringBuffer(x) for x in "abc"]
    plus = node(func=lambda x, y: f"({x} + {y})", inputs=(a, b), outputs=(c,))
    nodes = [get_node(plus)]
    _run_graph(NodeGraph.from_nodes(nodes))
    assert c.load() == "c(a + b)"


def test_run_parametrized_all():
    a, b, c, d, e, f = [StringBuffer(x) for x in "abcdef"]
    plus = node(func=lambda x, y: f"{x} + {y}", inputs=(a, b), outputs=(c,))
    minus = node(func=lambda x, y: f"{x} - {y}", inputs=(c, d), outputs=(e,))
    square = node(func=lambda x: f"({x})^2", inputs=(e,), outputs=(f,))
    run(plus, minus, square)
    assert c.load() == "ca + b"
    assert e.load() == "ea + b - d"
    assert f.load() == "f(a + b - d)^2"


def test_run_parametrized_two():
    a, b, c, d, e = [StringBuffer(x) for x in "abcde"]
    plus = node(func=lambda x, y: f"{x} + {y}", inputs=(a, b), outputs=(c,))
    minus = node(func=lambda x, y: f"{x} - {y}", inputs=(c, d), outputs=(e,))
    run(plus, minus)
    assert c.load() == "ca + b"
    assert e.load() == "ea + b - d"


def test_run_parametrized_one():
    a, b, c = [StringBuffer(x) for x in "abc"]
    plus = node(func=lambda x, y: f"{x} + {y}", inputs=(a, b), outputs=(c,))
    run(plus)
    assert c.load() == "ca + b"
