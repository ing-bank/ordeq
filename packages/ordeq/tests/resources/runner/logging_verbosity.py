import logging

from ordeq import node
from ordeq._nodes import get_node
from ordeq._graph import NodeGraph
from ordeq._runner import _run_graph
from ordeq_common import StringBuffer

logging.basicConfig(level=logging.INFO)
A, B, C, D, E, F = [StringBuffer(c) for c in "ABCDEF"]

plus = node(func=lambda x, y: f"{x} + {y}", inputs=(A, B), outputs=(C,))
minus = node(func=lambda x, y: f"{x} - {y}", inputs=(C, D), outputs=(E,))
square = node(func=lambda x: f"({x})^2", inputs=(E,), outputs=(F,))

nodes = [get_node(n) for n in (plus, minus, square)]
_run_graph(NodeGraph.from_nodes(nodes))
