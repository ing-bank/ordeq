import inspect

from ordeq import node
from ordeq._nodes import _is_node
from ordeq_common import StringBuffer


@node(
    inputs=[StringBuffer("x"), StringBuffer("y")],
    outputs=[StringBuffer("z"), StringBuffer("1")],
)
def func(x: str, y: str) -> tuple[str, str]:
    return f"{x} + {y}", y


print(type(func))
print(func)
print(inspect.get_annotations(func))
print(_is_node(func))
