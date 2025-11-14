import tempfile
from pathlib import Path

from ordeq_viz import viz

with tempfile.TemporaryDirectory() as tmpdirname:
    tmp_path = Path(tmpdirname)
    output_file = tmp_path / "output.mermaid"

    viz(
        "example_rag_pipeline",
        fmt="mermaid",
        output=output_file,
        use_dataset_styles=True,
        legend=True,
        title="RAG Pipeline",
    )

    content = output_file.read_text()
    print(content)
