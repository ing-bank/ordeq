import logging
from pathlib import Path

from ordeq_viz import viz

from project_ml import catalog, data, deploy, model

ROOT_PATH = Path(__file__).parent.parent.parent

logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    pipeline = {data, model, deploy}
    viz(
        *pipeline,
        catalog,
        fmt="mermaid",
        output=ROOT_PATH / "pipeline_diagram.mermaid",
        subgraphs=True,
    )
    # run(*pipeline)
