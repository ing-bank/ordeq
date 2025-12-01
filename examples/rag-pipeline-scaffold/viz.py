from pathlib import Path

import rag_pipeline
from ordeq_viz import viz

if __name__ == "__main__":
    viz(
        rag_pipeline,
        fmt="mermaid",
        output=Path("rag_pipeline.mermaid"),
        legend=False,
    )
