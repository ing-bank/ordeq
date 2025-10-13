from ordeq import node
from ordeq._nodes import get_node


@node
def view() -> str:
    return "Hello, World!"


@node(inputs=view)
def n(v: str) -> None:
    print(f"Node received {v}")


print(repr(get_node(view)))
print(repr(get_node(n)))
