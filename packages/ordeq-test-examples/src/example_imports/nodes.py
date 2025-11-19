# ruff: noqa: PLC0415 (import inside function)
from ordeq import node


def scope():
    from example_imports.catalog import a as b

    @node(outputs=b)
    def hello() -> str:
        return "Hello, World!"
