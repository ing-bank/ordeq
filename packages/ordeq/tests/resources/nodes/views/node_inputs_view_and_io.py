from ordeq import node, run
from ordeq_common import Literal, Print


@node
def view() -> str:
    return "Hello, World!"


@node(inputs=[Literal("Jane"), view], outputs=Print())
def n(name: str, v: str) -> str:
    return f"{name} said {v}"


print(run(n, verbose=True))
