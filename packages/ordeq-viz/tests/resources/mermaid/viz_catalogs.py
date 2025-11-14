import example_catalogs
from ordeq._resolve import _resolve_runnables_to_nodes_and_ios

from ordeq_viz.to_mermaid import pipeline_to_mermaid

nodes, ios = _resolve_runnables_to_nodes_and_ios(example_catalogs)
diagram = pipeline_to_mermaid(nodes=nodes, ios=ios)
print(diagram)
