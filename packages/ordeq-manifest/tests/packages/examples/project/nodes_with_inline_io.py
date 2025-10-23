from ordeq import node, IO
from ordeq_common import Literal


@node(inputs=Literal("Buenos dias"), outputs=IO())
def greet(hello: str):
    print(hello)
