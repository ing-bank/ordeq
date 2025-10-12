from ordeq import node

from examples.project.catalog_1 import a, b
from examples.project.catalog_2 import f


@node(inputs=[a, b], outputs=f)
def func_a(a_val: str, b_val: str) -> str:
    return a_val + b_val


from examples.project import (  # noqa: E402 (import after other statements)
    catalog_1,
    catalog_2,
)


@node(
    inputs=[catalog_1.a, catalog_1.b],
    outputs=catalog_2.f,
    tags={"viz": "orange"},
)
def func_b(a_val: str, b_val: str) -> str:
    return a_val + b_val
