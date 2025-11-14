from ordeq import node
from ordeq_common import Print


@node(outputs=Print())
def hello() -> str:
    return "Hello, World!"


@node(inputs=hello)
def say_hello(value: str) -> str:
    return value
