from ordeq import node
from ordeq_common import Literal

A = Literal("A")
B = Literal("B")


@node(inputs=A)
def Ap(data: str) -> str:
    return data.lower()


@node(inputs=B)
def Bp(data: str) -> str:
    return data * 3


@node(inputs=[Ap, Bp])
def AB(a: str, b: str) -> str:
    return a + b


@node(inputs=AB)
def print_result(data: str) -> None:
    print(data)
