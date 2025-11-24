from ordeq import Input, Node, node, run
from ordeq_common import StringBuffer

greeting = Input("Hello")
buffer = StringBuffer()


@node(inputs=greeting, outputs=buffer)
def hello(hi: str) -> str:
    print("Saying", hi)
    return hi


@node(inputs=buffer)
def world(value: str) -> str:
    say = f"{value}, world!!"
    print("Saying", say)
    return say


def takes_greeting(n: Node) -> bool:
    return greeting in n.inputs


print("Should run only `hello` (filter returns False for `world`):")
run(hello, world, node_filter=takes_greeting)
