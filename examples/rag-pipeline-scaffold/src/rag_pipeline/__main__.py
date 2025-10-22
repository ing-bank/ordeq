from pathlib import Path

from ordeq_viz import viz

import rag_pipeline

if __name__ == "__main__":
    mermaid_path = Path(__file__).parent.parent.parent / "rag_pipeline.mermaid"
    viz(rag_pipeline, fmt="mermaid", output=mermaid_path)
