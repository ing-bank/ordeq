from ordeq import node, run, view
from ordeq._nodes import get_view
from ordeq_common import Literal


@view
def hello() -> str:
    return "Hello, World!"


print(repr(get_view(hello)))


@view(inputs=[Literal("Jane"), hello])
def hello_from_someone(name: str, v: str) -> str:
    return f"{name} said '{v}'"


print(repr(get_view(hello_from_someone)))


@node(inputs=hello_from_someone)
def n(v: str) -> None:
    print(f"I heard that {v}")


print(run(n, verbose=True))
