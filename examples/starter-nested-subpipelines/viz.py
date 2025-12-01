from pathlib import Path

import starter_nested_subpipelines
from ordeq_viz import viz

if __name__ == "__main__":
    viz(
        starter_nested_subpipelines,
        fmt="mermaid",
        output=Path("diagram.mermaid"),
        legend=False,
    )
