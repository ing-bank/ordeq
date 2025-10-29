from ordeq import node
from ordeq_common import Literal, Print

greeting = Literal("Hello")
printer = Print()


@node(inputs=greeting)
def greet(hello: str):
    print(hello)


@node(inputs=greeting, outputs=printer)
def farewell(g: str) -> str:
    return f"{g}; Goodbye!"
