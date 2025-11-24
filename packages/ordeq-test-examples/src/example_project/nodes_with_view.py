from ordeq import Input, node
from ordeq_common import Print

greeting = Input[str]("Hello")
printer = Print()


@node(inputs=greeting)
def greet(hello: str):
    return hello


@node(inputs=greet, outputs=printer)
def farewell(g: str) -> str:
    return f"{g}; Goodbye!"
