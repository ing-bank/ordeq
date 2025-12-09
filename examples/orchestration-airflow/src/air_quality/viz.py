from ordeq_viz import viz

import air_quality
from air_quality.paths import PROJECT_ROOT

if __name__ == "__main__":
    viz(
        air_quality,
        fmt="mermaid",
        output=PROJECT_ROOT / "air_quality.mermaid",
        legend=False,
    )
