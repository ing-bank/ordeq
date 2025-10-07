from ordeq import node
from ordeq_common import StringBuffer, Literal

x = Literal("X")


@node(inputs=x, outputs=x)  # outputs should be of type Output or IO
def func(data: str) -> str:
    return data + data
