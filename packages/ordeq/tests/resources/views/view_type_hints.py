import inspect
from typing_extensions import reveal_type

from ordeq import node
from ordeq._nodes import _is_node
from ordeq_common import StringBuffer


@node(inputs=[StringBuffer("x"), StringBuffer("y")])
def func(x: str, y: str) -> tuple[str, str]:
    return f"{x} + {y}", y


reveal_type(func)
print(type(func))
print(func)
print(inspect.get_annotations(func))
print(_is_node(func))
