from ordeq._resolve import _resolve_runnables_to_nodes_and_ios
from ordeq_viz import pipeline_to_mermaid

import example  # ty: ignore[unresolved-import]


nodes, ios = _resolve_runnables_to_nodes_and_ios(example)
diagram = pipeline_to_mermaid(nodes=nodes, ios=ios)
print(diagram)

print("-" * 40)

diagram = pipeline_to_mermaid(
    nodes=nodes, ios=ios, connect_wrapped_datasets=False
)
print(diagram)
