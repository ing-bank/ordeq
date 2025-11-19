from example_async import async_ios
from ordeq import run
from ordeq_viz import viz

print(viz(async_ios, fmt="mermaid"))
run(async_ios)
