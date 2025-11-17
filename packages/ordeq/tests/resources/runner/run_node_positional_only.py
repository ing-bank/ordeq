from ordeq import node, run
from ordeq_common import Literal


@node(inputs=[Literal("a"), Literal("b")])
def my_node(a, /, b):
    print(f"a: {a}, b: {b}")


run(my_node)
