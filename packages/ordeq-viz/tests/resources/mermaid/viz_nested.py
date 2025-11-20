import example_nested

from ordeq_viz import viz

diagram = viz(example_nested, fmt="mermaid", subgraphs=True)
print(diagram)
