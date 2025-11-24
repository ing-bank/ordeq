from ordeq import Input, Node, node, run
from ordeq_common import Print

greeting = Input[str]("Hello")


@node(inputs=greeting, prints=False)
def hello(hi: str) -> str:
    return hi


@node(inputs=hello, outputs=Print(), prints=True)
def world(value: str) -> str:
    say = f"{value}, world!!"
    print("Saying", say)
    return say


def prints(n: Node) -> bool:
    return n.attributes.get("prints", False)


print("Should run both `hello` and `world`:")
# Even though the filter only returns True for `world`, `hello` is a view
# and is run because `world` is run.
run(hello, world, node_filter=prints, verbose=True)

print("Should run neither `hello` nor `world`:")
run(hello, node_filter=prints, verbose=True)

print("Should run both `hello` and `world`:")
run(world, node_filter=prints, verbose=True)
