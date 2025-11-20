import example_2

from ordeq_viz import viz

diagram = viz(example_2, fmt="mermaid", subgraphs=True)
print(diagram)
