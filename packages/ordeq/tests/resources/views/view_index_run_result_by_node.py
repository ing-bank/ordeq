from ordeq import node, run
from ordeq._nodes import get_node
from ordeq_common import Print


@node
def view() -> str:
    return "Hello!"


@node(inputs=view, outputs=Print())
def hello(data: str) -> None:
    print(data)


result = run(hello)
print(view, 'computed', result[get_node(view)])
