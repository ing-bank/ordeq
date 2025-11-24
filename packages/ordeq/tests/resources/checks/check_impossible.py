from ordeq import Input, node, run
from ordeq_common import StringBuffer

hello = Input("hello")
world = StringBuffer()


@node(inputs=hello, outputs=world)
def simple_node(hello: str) -> str:
    return hello + " world"


@node(inputs=[hello, world], checks=[hello, world])
def check_impossible(hello: str, world: str) -> None:
    print(hello, world)


if __name__ == "__main__":
    print("Expected output is an error due to impossible check")
    run(__name__)
