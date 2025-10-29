from ordeq import IO, node, run
from ordeq_common import Literal, SpyHook

spy = SpyHook()


@node(inputs=Literal("name"), outputs=IO())
def hello(name: str) -> str:
    return f"Hello, {name}!"


@node
def fail() -> None:
    raise ValueError("Intentional failure for testing.")


run(hello, hooks=[spy])
print(spy.called_with)

run(fail, hooks=[spy])
print(spy.called_with)
