## Resource

```python
# Checks the behaviour when running nodes with an alternative catalog
# We want to support this syntax and behaviour since it allows users to
# easily switch between different catalogs, for instance during tests.
from example_catalogs import local, local_package
from ordeq import node, run
from ordeq_common import Print

catalog = local


@node(inputs=catalog.hello, outputs=catalog.result)
def uppercase(hello: str) -> str:
    return f"{hello.upper()}!"


@node(inputs=catalog.result, outputs=Print())
def add_world(hello: str) -> str:
    return f"{hello}, world!!"


run(uppercase, add_world, io={local: local_package})

```

## Output

```text
HELLO FROM LOCAL PACKAGE!, world!!

```

## Logging

```text
INFO	ordeq.io	Loading StringBuffer(_buffer=<_io.StringIO object at HASH1>)
INFO	ordeq.runner	Running node "uppercase" in module "run_io_catalog_package"
INFO	ordeq.io	Saving StringBuffer(_buffer=<_io.StringIO object at HASH2>)
INFO	ordeq.runner	Running node "add_world" in module "run_io_catalog_package"
INFO	ordeq.io	Saving Print()

```