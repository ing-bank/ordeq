from ordeq import node, run
from ordeq_common import Literal, StringBuffer

greeting = Literal("Hello")
buffer = StringBuffer()


@node(inputs=greeting, outputs=buffer)
def hello(hi: str) -> str:
    print("Saying", hi)
    return hi


@node(inputs=buffer)
def world(value: str) -> str:
    say = f"{value}, world!"
    print("Saying", say)
    return say


print("Should run all nodes (node filter maps all nodes to True):")
run(hello, world, node_filter=lambda n: True)

print("Should run no nodes (node filter maps all nodes to False):")
run(hello, world, node_filter=lambda n: False)
