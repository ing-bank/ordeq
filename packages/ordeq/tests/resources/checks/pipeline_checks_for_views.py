from example_checks import pipeline_checks_for_views
from ordeq import run
from ordeq_viz import viz

if __name__ == "__main__":
    print(viz(pipeline_checks_for_views, fmt="mermaid"))

    print("Expected output is 'aBBB'")
    run(pipeline_checks_for_views)
