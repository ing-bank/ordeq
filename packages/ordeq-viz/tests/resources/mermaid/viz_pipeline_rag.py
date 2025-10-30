from ordeq_viz import viz

diagram = viz(
    "example_rag_pipeline",
    fmt="mermaid",
    io_shape_template='("{value}")',
    use_dataset_styles=True,
    legend=True,
    title="RAG Pipeline",
)
print(diagram)
