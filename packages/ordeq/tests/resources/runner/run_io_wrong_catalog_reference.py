# Checks the behaviour when running nodes with a reference to an alternative
# catalog. We want to support this syntax and behaviour since it allows users
# to switch between catalogs without having to import the catalog.
from example_catalogs import local
from ordeq import node, run

catalog = local


@node(inputs=catalog.hello, outputs=catalog.result)
def uppercase(hello: str) -> str:
    return f"{hello.upper()}!"


# NOK: IO references need to be formatted 'module.submodule.[...]'
run(uppercase, io={catalog.hello: "example_catalogs:remote"})
