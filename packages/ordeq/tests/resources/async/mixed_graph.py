from example_async import mixed_graph
from ordeq import run
from ordeq_viz import viz

print(viz(mixed_graph, fmt="mermaid"))
run(mixed_graph)
