from ordeq import node, run
from ordeq_common import Literal, Print


@node
def view() -> str:
    return "Hello, World!"


@node(inputs=[Literal("Jane"), view])
def another_view(name: str, v: str) -> str:
    return f"{name} said {v}"


@node(inputs=another_view)
def n(v: str) -> None:
    print(f"Node received {v}")


print(run(n, verbose=True))
