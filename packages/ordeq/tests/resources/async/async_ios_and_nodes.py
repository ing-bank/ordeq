from example_async import async_ios_and_nodes
from ordeq import run
from ordeq_viz import viz

print(viz(async_ios_and_nodes, fmt="mermaid"))
run(async_ios_and_nodes)
print(async_ios_and_nodes.buffer_3.load())
