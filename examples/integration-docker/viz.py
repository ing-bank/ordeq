from pathlib import Path

import integration_docker
from ordeq_viz import viz

if __name__ == "__main__":
    viz(
        integration_docker,
        fmt="mermaid",
        output=Path("diagram.mermaid"),
        legend=False,
    )
