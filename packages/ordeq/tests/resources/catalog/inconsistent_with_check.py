from ordeq import node
from ordeq.catalog import check_catalogs_are_consistent

from resources.catalog.catalogs import inconsistent, local

check_catalogs_are_consistent(local, inconsistent)
catalog = inconsistent


@node(inputs=catalog.hello, outputs=catalog.result)
def func(hello: str) -> str:
    return f"{hello.upper()}!"
