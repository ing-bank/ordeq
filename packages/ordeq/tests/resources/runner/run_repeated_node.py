from ordeq import node, run
from ordeq_common import StringBuffer

x = StringBuffer()


@node(outputs=x)
def func1() -> str:
    return "Hello"


run(func1, func1)
