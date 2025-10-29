from ordeq import IO, node
from ordeq_common import Print

x = IO[str]()
y = Print()


@node(inputs=x, outputs=y, tags=["dummy"])
def func(something: str) -> str:
    return something
