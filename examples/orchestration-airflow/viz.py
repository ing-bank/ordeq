from pathlib import Path

import air_quality_insights
from ordeq_viz import viz

if __name__ == "__main__":
    viz(
        air_quality_insights,
        fmt="mermaid",
        output=Path("air_quality_insights.mermaid"),
        legend=False,
    )
