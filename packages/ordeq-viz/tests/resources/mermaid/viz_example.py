from example_1 import nodes as mod
from ordeq._nodes import get_node

from ordeq_viz.graph import _gather_graph
from ordeq_viz.to_mermaid import graph_to_mermaid

diagram = graph_to_mermaid(
    _gather_graph(
        nodes=[get_node(mod.world)], ios={"...": {"x": mod.x, "y": mod.y}}
    )
)
print(diagram)
