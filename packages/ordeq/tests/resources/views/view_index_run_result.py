from ordeq import node, run
from ordeq_common import Print


@node
def view() -> str:
    return "Hello!"


@node(inputs=view, outputs=Print())
def hello(data: str) -> None:
    print(data)


result = run(hello)
# This should work, but it doesn't because
print(view, 'computed', result[view])
