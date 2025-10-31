# Checks the behaviour when running nodes with an alternative catalog
# We want to support this syntax and behaviour since it allows users to
# easily switch between different catalogs, for instance during tests.
from example_catalogs import remote_package, local_package
from ordeq import node, run
from ordeq_common import Print

catalog = local_package


@node(inputs=catalog.hello, outputs=catalog.result)
def uppercase(hello: str) -> str:
    return f"{hello.upper()}!"


@node(inputs=catalog.result, outputs=Print())
def add_world(hello: str) -> str:
    return f"{hello}, world!!"


run(uppercase, add_world, io={catalog: remote_package})
