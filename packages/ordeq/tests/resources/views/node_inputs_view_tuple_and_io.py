from ordeq import node, run
from ordeq_common import Literal, Print


@node
def hello() -> tuple[str, str]:
    return "Hello", "world"


print(repr(hello))


@node(inputs=[hello, Literal("!!!")], outputs=Print())
def combine_greeting_with_ending(greeting: tuple[str, str], e: str):
    return f"{' '.join(greeting)} {e}"


run(combine_greeting_with_ending, verbose=True)
