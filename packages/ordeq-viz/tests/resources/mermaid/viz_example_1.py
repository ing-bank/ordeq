import example_1
from ordeq._resolve import _resolve_runnables_to_nodes_and_ios

from ordeq_viz.to_mermaid import pipeline_to_mermaid

fqn_nodes, ios = _resolve_runnables_to_nodes_and_ios(example_1)
nodes = [node for _, _, node in fqn_nodes]
diagram = pipeline_to_mermaid(nodes=nodes, ios=ios, subgraphs=True)
print(diagram)
