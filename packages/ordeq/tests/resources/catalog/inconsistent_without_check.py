from example_catalogs import inconsistent as catalog
from ordeq import node


@node(inputs=catalog.hello, outputs=catalog.result)
def func(hello: str) -> str:
    return f"{hello.upper()}!"
