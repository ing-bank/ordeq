from ordeq import node, run, view
from ordeq_common import Print


@view
def greeting() -> str:
    return "Hello, World!"


@node(inputs=greeting, outputs=Print())
def n(name: str, v: str) -> str:
    return f"{name} said {v}"


print(run(n, verbose=True))
