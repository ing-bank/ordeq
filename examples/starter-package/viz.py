from pathlib import Path

import starter_package
from ordeq_viz import viz

if __name__ == "__main__":
    viz(
        starter_package,
        fmt="mermaid",
        output=Path("diagram.mermaid"),
        legend=False,
    )
