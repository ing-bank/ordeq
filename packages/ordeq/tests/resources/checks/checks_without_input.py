from ordeq import Input, node, run
from ordeq_viz import viz

A = Input("A")


@node(checks=[A])
def my_node():
    print("This node is required before running anything else on A")


@node(inputs=[A])
def dependent_node(data: str):
    print(f"Dependent node received data: {data}")


if __name__ == "__main__":
    print(viz(__name__, fmt="mermaid"))
    run(__name__)
