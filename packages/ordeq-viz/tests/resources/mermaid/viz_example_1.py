import example_1

from ordeq_viz import viz

diagram = viz(example_1, fmt="mermaid", subgraphs=True)
print(diagram)
