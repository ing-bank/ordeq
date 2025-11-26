from ordeq_viz import viz

diagram = viz(
    "example_rag_pipeline",
    fmt="mermaid",
    use_dataset_styles=True,
    legend=True,
    title="RAG Pipeline",
    subgraphs=True,
)
print(diagram)
