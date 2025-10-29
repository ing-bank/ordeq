import logging

from ordeq import IO, node, run
from ordeq_common import Literal, LoggerHook

_logger = logging.getLogger("custom_logger")
_logger.setLevel(logging.CRITICAL)
logger = LoggerHook(logger=_logger)


@node(inputs=Literal("name"), outputs=IO())
def hello(name: str) -> str:
    return f"Hello, {name}!"


@node
def fail() -> None:
    raise ValueError("Intentional failure for testing.")


run(hello, hooks=[logger])

run(fail, hooks=[logger])
