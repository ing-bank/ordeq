from ordeq import node
from project.catalog_1 import a
from project.catalog_1 import b as B
from project.catalog_2 import f


@node(inputs=[a, B], outputs=f, tags={"key": "threshold", "value": 0.23})
def func(a_val: str, b_val: str) -> str:
    return a_val + b_val
