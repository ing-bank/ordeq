from ordeq import IO, node, run
from ordeq_common import Literal, StringBuffer
from ordeq_viz import viz

A = Literal("A")
B = Literal("B")
Ap = IO()
Bp = IO()
AB = StringBuffer()


@node(inputs=A, outputs=Ap)
def process_a(data: str) -> str:
    return data.lower()


@node(inputs=B, outputs=Bp)
def process_b(data: str) -> str:
    return data * 3


@node(inputs=[Ap, Bp], outputs=AB)
def join(a: str, b: str) -> str:
    return a + b


@node(inputs=AB)
def print_result(data: str) -> None:
    print(data)


if __name__ == "__main__":
    print(viz(__name__, fmt="mermaid"))
    run(__name__)
