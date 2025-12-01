from pathlib import Path

import kedro_spaceflights
from ordeq_viz import viz

if __name__ == "__main__":
    viz(
        kedro_spaceflights,
        fmt="mermaid",
        output=Path("diagram.mermaid"),
        legend=False,
    )
