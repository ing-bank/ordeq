import tempfile
from pathlib import Path

import rag_pipeline  # ty: ignore[unresolved-import]  # noqa: F401,RUF100

from ordeq_viz import viz

with tempfile.TemporaryDirectory() as tmpdirname:
    tmp_path = Path(tmpdirname)
    output_file = tmp_path / "output.mermaid"

    viz(
        "rag_pipeline",
        fmt="mermaid",
        output=output_file,
        io_shape_template="({value})",
        use_dataset_styles=True,
        legend=True,
        title="RAG Pipeline",
    )

    content = output_file.read_text()
    print(content)
