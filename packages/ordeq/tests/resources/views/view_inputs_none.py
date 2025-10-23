from ordeq import node
from ordeq._nodes import get_node


@node(None)
def my_view() -> None:
    print("Hello, world!")


print(repr(get_node(my_view)))
