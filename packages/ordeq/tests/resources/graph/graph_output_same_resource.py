# Captures creation of a graph in case of node cycles
from example_resources import same_output
from ordeq._graph import BaseGraph
from ordeq._resolve import _resolve_runnables_to_nodes

nodes = _resolve_runnables_to_nodes(same_output)
_ = BaseGraph.from_nodes(*nodes)
