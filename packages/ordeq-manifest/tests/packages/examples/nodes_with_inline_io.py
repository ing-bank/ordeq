from ordeq import node
from ordeq_common import Literal


@node(inputs=Literal("Buenos dias"))
def greet(hello: str):
    print(hello)
