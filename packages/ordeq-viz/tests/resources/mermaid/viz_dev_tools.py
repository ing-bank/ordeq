import ordeq_dev_tools
from ordeq._resolve import _resolve_runnables_to_nodes_and_ios

from ordeq_viz.to_mermaid import pipeline_to_mermaid

nodes, ios = _resolve_runnables_to_nodes_and_ios(ordeq_dev_tools)
diagram = pipeline_to_mermaid(nodes=nodes, ios=ios)
print(diagram)
