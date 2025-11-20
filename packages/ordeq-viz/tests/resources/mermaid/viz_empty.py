import example_empty

from ordeq_viz import viz

diagram = viz(example_empty, fmt="mermaid", subgraphs=True)
print(diagram)
