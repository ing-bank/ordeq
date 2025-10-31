## Resource

```python
# Checks the behaviour when running nodes with an alternative catalog
# We want to support this syntax and behaviour since it allows users to
# easily switch between different catalogs, for instance during tests.
from example_catalogs import inconsistent, local
from ordeq import node, run
from ordeq_common import Print

catalog = local


@node(inputs=catalog.hello, outputs=catalog.result)
def uppercase(hello: str) -> str:
    return f"{hello.upper()}!"


@node(inputs=catalog.result, outputs=Print())
def add_world(hello: str) -> str:
    return f"{hello}, world!!"


run(uppercase, add_world, io={catalog: inconsistent})

```

## Output

```text
HELLO FROM LOCAL!HELLO FROM LOCAL!HELLO FROM REMOTE!, world!!

```

## Logging

```text
INFO	ordeq.io	Loading StringBuffer(_buffer=<_io.StringIO object at HASH1>)
INFO	ordeq.runner	Running node "uppercase" in module "run_io_catalog_inconsistent"
INFO	ordeq.io	Saving StringBuffer(_buffer=<_io.StringIO object at HASH2>)
INFO	ordeq.runner	Running node "add_world" in module "run_io_catalog_inconsistent"
INFO	ordeq.io	Saving Print()

```