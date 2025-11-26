import ordeq_dev_tools

from ordeq_viz import viz

diagram = viz(ordeq_dev_tools, fmt="mermaid", subgraphs=True)
print(diagram)
