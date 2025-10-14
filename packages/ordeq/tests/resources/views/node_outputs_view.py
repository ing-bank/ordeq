from ordeq import node
from ordeq._nodes import get_node


@node
def view() -> str:
    return "Hello, World!"


@node(outputs=view)
def hello() -> None:
    print("Hello world!")


print(repr(get_node(hello)))
