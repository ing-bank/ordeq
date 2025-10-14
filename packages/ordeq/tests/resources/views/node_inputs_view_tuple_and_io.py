from ordeq import node, run, view
from ordeq._nodes import get_view
from ordeq_common import Literal, Print


@view
def hello() -> tuple[str, str]:
    return "Hello", "world"


print(repr(get_view(hello)))


@node(inputs=[hello, Literal("!!!")], outputs=Print())
def combine_greeting_with_ending(greeting: tuple[str, str], e: str):
    return f"{' '.join(greeting)} {e}"


print(run(combine_greeting_with_ending, verbose=True))
