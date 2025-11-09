# Captures creation of a graph in case of node cycles
from example_resources import cycle
from ordeq._graph import BaseGraph
from ordeq._resolve import _resolve_runnables_to_nodes

nodes = _resolve_runnables_to_nodes(cycle)
base_graph = BaseGraph.from_nodes(nodes)
