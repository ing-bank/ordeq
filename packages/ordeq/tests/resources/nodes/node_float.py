# Captures the behaviour when a node is created with a non-supported argument.
from ordeq import node


@node(0.123)
def my_node() -> None:
    print("Hello, world!")
