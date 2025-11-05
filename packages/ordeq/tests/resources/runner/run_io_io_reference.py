# Checks the behaviour when running nodes with a reference to an alternative
# catalog. We want to support this syntax and behaviour since it allows users
# to switch between catalogs without having to import the catalog.
from example_catalogs import local, remote
from ordeq import node, run
from ordeq_common import Print

catalog = local


@node(inputs=catalog.hello, outputs=catalog.result)
def uppercase(hello: str) -> str:
    return f"{hello.upper()}!"


@node(inputs=catalog.result, outputs=Print())
def add_world(hello: str) -> str:
    return f"{hello.upper()}, world!!"


# OK: an IO can be substituted by a reference to an IO
run(uppercase, add_world, io={catalog.hello: "example_catalogs.remote:hello"})

# OK: a reference to an IO can be substituted by a reference to an IO
run(
    uppercase,
    add_world,
    io={"example_catalogs.local:hello": "example_catalogs.remote:hello"},
)

# OK: a reference to an IO can be substituted by an IO
run(uppercase, add_world, io={"example_catalogs.local:hello": remote.hello})
