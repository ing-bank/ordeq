import logging

from ordeq import node, IO, run
from ordeq_common import Literal, LoggerHook

logger = LoggerHook(logging.getLogger("custom_logger"))


@node(inputs=Literal("name"), outputs=IO())
def hello(name: str) -> str:
    return f"Hello, {name}!"


@node
def fail() -> None:
    raise ValueError("Intentional failure for testing.")


run(hello, hooks=[logger])

run(fail, hooks=[logger])
