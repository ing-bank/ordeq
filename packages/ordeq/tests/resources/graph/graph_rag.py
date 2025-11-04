# Captures the behaviour when resolving a package catalog to IO.
from pprint import pprint

import example_rag_pipeline
from ordeq._graph import NodeGraph, NodeIOGraph
from ordeq._resolve import _resolve_runnables_to_nodes

nodes = _resolve_runnables_to_nodes(example_rag_pipeline)
base_graph = NodeIOGraph.from_nodes(nodes)
print(base_graph)
node_graph = NodeGraph.from_graph(base_graph)
pprint(node_graph.topological_ordering)
