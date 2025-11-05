from ordeq import IO, node
from ordeq_common import Literal, Print

greeting = Literal("Hello")
regular = IO()
alternative = Print()


@node(inputs=greeting, outputs=regular)
def hello(s: str):
    return f"{s}!"
