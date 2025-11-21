from example_checks import pipeline_base
from ordeq import run
from ordeq_viz import viz

if __name__ == "__main__":
    print(viz(pipeline_base, fmt="mermaid"))

    print("Expected output is 'aBBB'")
    run(pipeline_base)
