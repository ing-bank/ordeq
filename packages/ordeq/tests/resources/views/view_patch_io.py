from ordeq import node, run
from ordeq_common import Literal

hello_io = Literal("Hello")


@node(inputs=hello_io)
def hello_world(hello: str) -> tuple[str, str]:
    return hello, "World!"


@node(inputs=hello_world)
def n(v: tuple[str, ...]):
    print(f"Node received '{' '.join(v)}'")


print(run(n, verbose=True, io={hello_io: Literal("Buenos dias")}))
