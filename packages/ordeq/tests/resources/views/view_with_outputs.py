from ordeq import node, run
from ordeq_common import Print


@node(outputs=Print())
def view() -> tuple[str, str]:
    return "Hello", "World!"


@node(inputs=view)
def n(v: tuple[str, str]):
    print(f"Node received {v}")


print(run(n, verbose=True))
