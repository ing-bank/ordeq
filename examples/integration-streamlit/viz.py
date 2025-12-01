from pathlib import Path

import integration_streamlit
from ordeq_viz import viz

if __name__ == "__main__":
    viz(
        integration_streamlit,
        fmt="mermaid",
        output=Path("diagram.mermaid"),
        legend=False,
    )
