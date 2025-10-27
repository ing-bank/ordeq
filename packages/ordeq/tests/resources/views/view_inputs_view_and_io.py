from ordeq import node, run
from ordeq._nodes import get_node
from ordeq_common import Literal


@node
def hello() -> str:
    return "Hello, World!"


print(repr(get_node(hello)))


@node(inputs=[Literal("Jane"), hello])
def hello_from_someone(name: str, v: str) -> str:
    return f"{name} said '{v}'"


print(repr(get_node(hello_from_someone)))


@node(inputs=hello_from_someone)
def n(v: str) -> None:
    print(f"I heard that {v}")


print(run(n, verbose=True))
