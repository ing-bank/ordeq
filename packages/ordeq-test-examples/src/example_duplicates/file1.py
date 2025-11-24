from typing import Any

from ordeq import IO, Input, node

x_value = Input(3)
y_value = IO[Any]()


@node(inputs=x_value, outputs=y_value)
def foo(x: int) -> int:
    return x + 3
