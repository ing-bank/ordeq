from example import nodes as mod  # ty: ignore[unresolved-import]
from ordeq._nodes import get_node

from ordeq_viz.to_mermaid import pipeline_to_mermaid

diagram = pipeline_to_mermaid(
    nodes={get_node(mod.world)},
    ios={("...", "x"): mod.x, ("...", "y"): mod.y},
    io_shape_template='("{value}")',
    node_shape_template='("{value}")',
)
print(diagram)
