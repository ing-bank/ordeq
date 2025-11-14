from ordeq import node, run
from ordeq._nodes import get_node
from ordeq_common import Print


@node
def hello() -> str:
    return "Hello, World!"


print(repr(get_node(hello)))


@node(inputs=hello, outputs=Print())
def n(greeting: str) -> str:
    return f"She said '{greeting}'"


run(n, verbose=True)
