import example_project

from ordeq_viz import viz

result = viz(
    example_project,
    fmt="mermaid-md",
    node_filter=lambda n: n.attributes.get("tags", "x") != "x",
    output=None,
)
print(result)
