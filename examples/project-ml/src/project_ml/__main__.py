import logging
from pathlib import Path

import catalog
import data
import deploy
import model
from ordeq import run
from ordeq_viz import viz

ROOT_PATH = Path(__file__).parent.parent.parent

logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    pipeline = {data, model, deploy}
    viz(
        *pipeline,
        catalog,
        fmt="mermaid",
        output=ROOT_PATH / "pipeline_diagram.mermaid",
    )
    run(*pipeline)
