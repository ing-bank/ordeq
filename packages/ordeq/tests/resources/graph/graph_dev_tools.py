# Capture the graph representation and topological ordering
from pprint import pprint

import ordeq_dev_tools
from ordeq._graph import NamedNodeGraph, NamedNodeIOGraph
from ordeq._resolve import _resolve_runnables_to_nodes

nodes = _resolve_runnables_to_nodes(ordeq_dev_tools)
named_node_io_graph = NamedNodeIOGraph.from_nodes(nodes)
print("NamedNodeIOGraph:")
pprint(named_node_io_graph)

named_node_graph = NamedNodeGraph.from_graph(named_node_io_graph)
print("NamedNodeGraph:")
print(named_node_graph)

print("Topological ordering:")
pprint(named_node_graph.topological_ordering)
