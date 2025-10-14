from ordeq import node, run
from ordeq_common import Print

printer = Print()


@node(outputs=printer)
def view() -> str:
    return "Hello, World!"


@node(inputs=view)
def n(v: str) -> None:
    print(f"Node received {v}")


run(n, verbose=True)
