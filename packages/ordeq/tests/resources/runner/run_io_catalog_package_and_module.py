# Checks the behaviour when running nodes with an alternative catalog
# We want to support this syntax and behaviour since it allows users to
# easily switch between different catalogs, for instance during tests.
from example_catalogs import local_package, remote_extended, remote_package, \
    local
from ordeq import node, run
from ordeq_common import Print

catalog = local_package


@node(inputs=local_package.hello, outputs=remote_extended.hello)
def uppercase(hello: str) -> str:
    return f"{hello.upper()}!"


@node(inputs=remote_extended.another_io, outputs=Print())
def add_world(hello: str) -> str:
    return f"{hello}, world!!"


run(uppercase, add_world,
    io={local_package: remote_package, remote_extended: local}
    )
