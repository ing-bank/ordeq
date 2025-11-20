from example_async import async_ios
from ordeq import run
from ordeq_viz import viz

print(viz(async_ios, fmt="mermaid"))
print(
    "Expect the 'process_fast_string' node to complete "
    "before 'process_slow_string'"
)
run(async_ios)
print(async_ios.combined_result.load())
