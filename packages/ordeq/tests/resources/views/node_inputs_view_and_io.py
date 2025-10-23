from ordeq import node, run
from ordeq._nodes import get_node
from ordeq_common import Literal, Print


@node
def hello() -> str:
    return "Hello, World!"


print(repr(get_node(hello)))


@node(inputs=[Literal("Jane"), hello], outputs=Print())
def n(name: str, greeting: str) -> str:
    return f"{name} said '{greeting}'"


print(run(n, verbose=True))
