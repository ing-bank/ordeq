from ordeq import node
from ordeq._nodes import get_node


@node
def view() -> str:
    return "Hello, World!"


@node(inputs=view)
def n(v: str):
    print(f"Node received {v}")


print(get_node(view))
print(get_node(n))
