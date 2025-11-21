from example_checks import pipeline_checks_as_checks
from ordeq import run
from ordeq_viz import viz

if __name__ == "__main__":
    print(viz(pipeline_checks_as_checks, fmt="mermaid"))

    print("Expected output is 'aBBB'")
    run(pipeline_checks_as_checks)
