# Capture the graph representation and topological ordering
from pprint import pprint

import example_project
from ordeq._graph import NamedNodeGraph, NodeIOGraph
from ordeq._resolve import _resolve_runnables_to_nodes

nodes = _resolve_runnables_to_nodes(example_project)
node_io_graph = NodeIOGraph.from_nodes(*nodes)
named_node_graph = NamedNodeGraph.from_graph(node_io_graph)
print("NamedNodeGraph:")
print(named_node_graph)

print("Topological ordering:")
pprint(named_node_graph.topological_ordering)
