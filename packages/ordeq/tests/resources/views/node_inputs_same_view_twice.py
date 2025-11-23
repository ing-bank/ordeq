from ordeq import node, run
from ordeq_common import Print


@node
def hello() -> str:
    return "Hello, World!"


print(repr(hello))


@node(inputs=[hello, hello], outputs=Print())
def n(fst: str, snd: str) -> str:
    return f"{fst} == {snd}'"


run(n, verbose=True)
