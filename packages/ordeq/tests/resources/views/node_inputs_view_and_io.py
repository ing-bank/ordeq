from ordeq import Input, node, run
from ordeq_common import Print


@node
def hello() -> str:
    return "Hello, World!"


print(repr(hello))


@node(inputs=[Input("Jane"), hello], outputs=Print())
def n(name: str, greeting: str) -> str:
    return f"{name} said '{greeting}'"


run(n, verbose=True)
