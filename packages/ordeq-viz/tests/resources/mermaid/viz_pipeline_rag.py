import rag_pipeline  # ty: ignore[unresolved-import]  # noqa: F401,RUF100

from ordeq_viz import viz


diagram = viz(
    "rag_pipeline",
    fmt="mermaid",
    io_shape_template="({value})",
    use_dataset_styles=True,
    legend=True,
    title="RAG Pipeline",
)
print(diagram)
