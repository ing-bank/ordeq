from example_catalogs import inconsistent, local
from ordeq import node
from ordeq._catalog import check_catalogs_are_consistent

check_catalogs_are_consistent(local, inconsistent)
catalog = inconsistent


@node(inputs=catalog.hello, outputs=catalog.result)
def func(hello: str) -> str:
    return f"{hello.upper()}!"
