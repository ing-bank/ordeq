from ordeq import Input, node, run
from ordeq_common import Print


@node
def hello() -> tuple[str, str]:
    return "Hello", "world"


print(repr(hello))


@node(inputs=[hello, Input("!!!")], outputs=Print())
def combine_greeting_with_ending(greeting: tuple[str, str], e: str):
    return f"{' '.join(greeting)} {e}"


run(combine_greeting_with_ending, verbose=True)
