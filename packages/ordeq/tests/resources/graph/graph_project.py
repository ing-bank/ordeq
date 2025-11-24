# Capture the graph representation and topological ordering
from pprint import pprint

import example_project
from ordeq._graph import NodeGraph, NodeIOGraph
from ordeq._process_nodes import _collect_views
from ordeq._resolve import _resolve_runnables_to_nodes

fqn_nodes = _resolve_runnables_to_nodes(example_project)
fq_nodes_and_views = _collect_views(*fqn_nodes)
nodes_and_views = [node for _, node in fq_nodes_and_views]
base_graph = NodeIOGraph.from_nodes(nodes_and_views)
print("NodeIOGraph")
print(base_graph)

node_graph = NodeGraph.from_nodes(nodes_and_views)
print("NodeGraph")
print(node_graph)

print("Topological ordering")
pprint(node_graph.topological_ordering)
