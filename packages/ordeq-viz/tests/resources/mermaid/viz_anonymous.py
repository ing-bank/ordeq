import example_anonymous
from ordeq._resolve import _resolve_runnables_to_nodes_and_ios

from ordeq_viz.to_mermaid import pipeline_to_mermaid

nodes, ios = _resolve_runnables_to_nodes_and_ios(example_anonymous)
diagram = pipeline_to_mermaid(
    nodes=nodes, ios=ios, connect_wrapped_datasets=False
)
print(diagram)
