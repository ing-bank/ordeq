import example_catalogs

from ordeq_viz import viz

diagram = viz(example_catalogs, fmt="mermaid")
print(diagram)
