from ordeq import node, run, view
from ordeq._nodes import get_view
from ordeq_common import Literal, Print


@view
def hello() -> str:
    return "Hello, World!"


print(repr(get_view(hello)))


@node(inputs=[Literal("Jane"), hello], outputs=Print())
def n(name: str, greeting: str) -> str:
    return f"{name} said '{greeting}'"


print(run(n, verbose=True))
