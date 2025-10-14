from ordeq import node
from ordeq_viz import viz


@node
def hello() -> None:
    print("Hello world!")


print(viz(__name__, fmt="mermaid"))
