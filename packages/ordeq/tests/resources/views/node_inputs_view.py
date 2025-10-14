from ordeq import node, run, view
from ordeq._nodes import get_view
from ordeq_common import Print


@view
def hello() -> str:
    return "Hello, World!"


print(repr(get_view(hello)))


@node(inputs=hello, outputs=Print())
def n(greeting: str) -> str:
    return f"She said '{greeting}'"


print(run(n, verbose=True))
