from example_async import extended_graph
from ordeq import run
from ordeq_viz import viz

print(viz(extended_graph, fmt="mermaid"))
run(extended_graph)
