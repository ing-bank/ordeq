# Capture the graph representation and topological ordering
from pprint import pprint

import example_anonymous
from ordeq._graph import NamedNodeIOGraph, NodeGraph
from ordeq._resolve import _resolve_runnables_to_nodes

nodes = _resolve_runnables_to_nodes(example_anonymous)
named_node_io_graph = NamedNodeIOGraph.from_nodes(nodes)
print("NamedNodeIOGraph:")
pprint(named_node_io_graph)

named_node_graph = NodeGraph.from_graph(named_node_io_graph)
print("NamedNodeGraph:")
pprint(named_node_graph)

print("Topological ordering:")
pprint(named_node_graph.topological_ordering)
