from ordeq_viz import viz

result = viz("example_1", fmt="mermaidchart-url", output=None)
print(result)

result = viz(
    "example_1",
    fmt="mermaidchart-url",
    output=None,
    base_url="https://localhost:8080/mermaid-chart/",
)
print(result)
