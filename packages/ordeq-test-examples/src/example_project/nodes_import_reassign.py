from ordeq import node

from example_project.catalog_1 import a, b
from example_project.catalog_2 import i, j

A = a
B = b


@node(inputs=[A, B], outputs=i)
def func_a(a_val: str, b_val: str) -> str:
    return a_val + b_val


AA = a
BB = b


@node(inputs=[AA, BB], outputs=j)
def func_b(a_val: str, b_val: str) -> str:
    return a_val + b_val
