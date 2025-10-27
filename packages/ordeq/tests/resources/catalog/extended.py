from ordeq import node, run

from resources.catalog.catalogs import remote_overridden

catalog = remote_overridden


@node(inputs=catalog.hello, outputs=catalog.result)
def func1(hello: str) -> str:
    return f"{hello.upper()}!"


run(func1)
print(catalog.result.load())
