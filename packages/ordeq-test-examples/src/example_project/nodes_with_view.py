from ordeq import node
from ordeq_common import Print

printer = Print()


@node
def greet():
    return "Hello"


@node(inputs=greet, outputs=printer)
def farewell(g: str) -> str:
    return f"{g}; Goodbye!"
