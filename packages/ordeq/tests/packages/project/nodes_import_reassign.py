from ordeq import node
from project.catalog_1 import a, b
from project.catalog_2 import f

A = a
B = b


@node(inputs=[A, B], outputs=f)
def func_a(a_val: str, b_val: str) -> str:
    return a_val + b_val


AA = a
BB = b


@node(inputs=[AA, BB], outputs=f)
def func_b(a_val: str, b_val: str) -> str:
    return a_val + b_val
