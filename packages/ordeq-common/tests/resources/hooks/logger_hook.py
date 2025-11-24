from ordeq import IO, Input, node, run
from ordeq_common import LoggerHook

logger = LoggerHook()


@node(inputs=Input[str]("name"), outputs=IO())
def hello(name: str) -> str:
    return f"Hello, {name}!"


@node
def fail() -> None:
    raise ValueError("Intentional failure for testing.")


run(hello, hooks=[logger])

run(fail, hooks=[logger])
