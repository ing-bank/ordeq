import example_3

from ordeq_viz import viz

diagram = viz(example_3, fmt="mermaid", subgraphs=True)
print(diagram)
