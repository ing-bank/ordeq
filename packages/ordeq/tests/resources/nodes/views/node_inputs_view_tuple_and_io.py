from ordeq import node, run
from ordeq_common import Literal, Print


@node
def greeting() -> tuple[str, str]:
    return "Hello", "World!"


@node(inputs=[greeting, Literal("!!!")], outputs=Print())
def combine_greeting_with_ending(g: tuple[str, str], e: str):
    return f"{g}{e}"


print(run(combine_greeting_with_ending, verbose=True))
