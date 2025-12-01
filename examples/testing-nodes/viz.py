from pathlib import Path

import testing_nodes
from ordeq_viz import viz

if __name__ == "__main__":
    viz(
        testing_nodes,
        fmt="mermaid",
        output=Path("diagram.mermaid"),
        legend=False,
    )
