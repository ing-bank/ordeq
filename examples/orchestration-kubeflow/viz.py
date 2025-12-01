from pathlib import Path

import ml_pipeline
from ordeq_viz import viz

if __name__ == "__main__":
    viz(
        ml_pipeline,
        fmt="mermaid",
        output=Path("ml_pipeline.mermaid"),
        legend=False,
    )
