from ordeq import node
from ordeq._nodes import get_node


def func() -> str:
    return "Hello, World!"


@node(inputs=func)
def hello(data: str) -> None:
    print(data)


print(repr(get_node(hello)))
