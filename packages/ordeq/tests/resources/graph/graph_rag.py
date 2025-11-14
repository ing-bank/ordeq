# Capture the graph representation and topological ordering
from pprint import pprint

import example_rag_pipeline
from ordeq._graph import NodeGraph, NodeIOGraph, ProjectGraph
from ordeq._resolve import _resolve_runnables_to_nodes

nodes = _resolve_runnables_to_nodes(example_rag_pipeline)
project_graph = ProjectGraph.from_nodes(nodes)
print("Topological ordering:")
pprint(project_graph.topological_ordering)

node_io_graph = NodeIOGraph.from_graph(project_graph)
print("NodeIOGraph:")
print(node_io_graph)

node_graph = NodeGraph.from_graph(node_io_graph)
print("NodeGraph")
print(node_graph)

print("Topological ordering")
pprint([node.name for node in node_graph.topological_ordering])
