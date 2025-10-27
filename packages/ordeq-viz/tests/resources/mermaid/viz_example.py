from ordeq._nodes import get_node

from ordeq_viz.to_mermaid import pipeline_to_mermaid

from example import nodes as mod  # ty: ignore[unresolved-import]

diagram = pipeline_to_mermaid(
    nodes={("example", "world"): get_node(mod.world)},
    ios={("...", "x"): mod.x, ("...", "y"): mod.y},
)
print(diagram)
