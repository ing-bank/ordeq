from ordeq import node
from ordeq_common import Literal, Print

greeting = Literal("Hello")
printer = Print()


@node(inputs=greeting)
def greet(hello: str):
    return hello


@node(inputs=greet, outputs=printer)
def farewell(g: str) -> str:
    return f"{g}; Goodbye!"
