from ordeq import node

from example_project.catalog_1 import a
from example_project.catalog_1 import b
from example_project.catalog_2 import h


@node(inputs=[a, b], outputs=h, tags={"key": "threshold", "value": 0.23})
def func(a_val: str, b_val: str) -> str:
    return a_val + b_val
