from ordeq import node
from ordeq._nodes import get_node

view = node


@view
def my_view() -> str:
    return "Hello, World!"
