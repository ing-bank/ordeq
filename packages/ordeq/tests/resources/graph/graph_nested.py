# Capture the graph representation and topological ordering
from pprint import pprint

import example_nested
from ordeq._graph import NodeGraph, NodeIOGraph
from ordeq._resolve import _resolve_runnables_to_nodes

nodes = _resolve_runnables_to_nodes(example_nested)
node_io_graph = NodeIOGraph.from_nodes(nodes)
print("NodeIOGraph:")
print(node_io_graph)

node_graph = NodeGraph.from_graph(node_io_graph)
print("NodeGraph:")
print(node_graph)

print("Topological ordering:")
pprint(node_graph.topological_ordering)
