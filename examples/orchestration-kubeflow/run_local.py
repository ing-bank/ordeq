from pathlib import Path

import ml_pipeline
from ordeq import run
from ordeq_viz import viz

if __name__ == "__main__":
    run(ml_pipeline)
    viz(
        ml_pipeline,
        fmt="mermaid",
        output=Path(__file__).parent / "ml_pipeline.mermaid",
    )
