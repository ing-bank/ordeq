from ordeq import IO, Input, node
from ordeq_common import Print

greeting = Input("Hello")
regular = IO()
alternative = Print()


@node(inputs=greeting, outputs=regular)
def hello(s: str):
    return f"{s}!"
