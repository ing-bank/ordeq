from typing import Any

from ordeq import IO, node
from ordeq_common import Literal

x_value = Literal(3)
y_value = IO[Any]()


@node(inputs=x_value, outputs=y_value)
def foo(x: int) -> int:
    return x + 3
