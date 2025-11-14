import example_project
from ordeq._resolve import _resolve_runnables_to_nodes_and_ios

from ordeq_viz.to_mermaid import pipeline_to_mermaid

nodes, ios = _resolve_runnables_to_nodes_and_ios(example_project)
diagram = pipeline_to_mermaid(nodes=nodes, ios=ios, subgraphs=False)
print(diagram)
