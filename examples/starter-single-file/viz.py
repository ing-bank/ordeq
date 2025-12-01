from pathlib import Path

import single_file
from ordeq_viz import viz

if __name__ == "__main__":
    viz(
        single_file,
        fmt="mermaid",
        output=Path("diagram.mermaid"),
        legend=False,
    )
