from ordeq import node, run, view
from ordeq._nodes import get_view
from ordeq_common import Literal, Print


@view
def hello() -> str:
    return "Hello, World!"


print(repr(get_view(hello)))


@node(inputs=[hello, hello], outputs=Print())
def n(fst: str, snd: str) -> str:
    return f"{fst} == {snd}'"


print(run(n, verbose=True))
