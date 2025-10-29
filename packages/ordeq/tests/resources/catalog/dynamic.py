from ordeq import node, run

from resources.catalog.catalogs import local, remote

env = "test-local"


def get_catalog():
    return local if env == "test-local" else remote


catalog = get_catalog()


@node(inputs=catalog.hello, outputs=catalog.result)
def func1(hello: str) -> str:
    return f"{hello.upper()}!"


run(func1)
print(catalog.result.load())

env = "test-acceptance"
catalog = get_catalog()


@node(inputs=catalog.hello, outputs=catalog.result)
def func2(hello: str) -> str:
    return f"{hello.upper()}!"


run(func2)
print(catalog.result.load())
