from ordeq import node
from ordeq_common import StringBuffer


@node(
    inputs=[StringBuffer("x"), StringBuffer("y")],
    outputs=[StringBuffer("z"), StringBuffer("1")],
)
def func(x: str, y: str) -> tuple[str, str]:
    """A really nice node"""

    return f"{x} + {y}", y


print(func.__doc__)
print(func)
print(func.__annotations__)
print(func.__module__)
print("Should all print long representation:")
print(f"{func!r}")
print(repr(func))
