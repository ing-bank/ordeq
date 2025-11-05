## Resource

```python
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


# OK: a module can be substituted by a reference to a module
run(uppercase, add_world, io={local: "example_catalogs.remote"})

# OK: a reference to a module can be substituted by a reference to a module
run(
    uppercase,
    add_world,
    io={"example_catalogs.local": "example_catalogs.remote"},
)

# OK: a reference to a module can be substituted by a module
run(uppercase, add_world, io={"example_catalogs.local": remote})

```

## Output

```text
HELLO FROM REMOTE!HEY I AM OVERRIDING THE HELLO IO!HELLO FROM REMOTE!HELLO FROM REMOTE!HELLO FROM REMOTE!HEY I AM OVERRIDING THE HELLO IO!HELLO FROM REMOTE!, world!!
HELLO FROM REMOTE!HEY I AM OVERRIDING THE HELLO IO!HELLO FROM REMOTE!HELLO FROM REMOTE!HELLO FROM REMOTE!HEY I AM OVERRIDING THE HELLO IO!HELLO FROM REMOTE!HELLO FROM REMOTE!, world!!
HELLO FROM REMOTE!HEY I AM OVERRIDING THE HELLO IO!HELLO FROM REMOTE!HELLO FROM REMOTE!HELLO FROM REMOTE!HEY I AM OVERRIDING THE HELLO IO!HELLO FROM REMOTE!HELLO FROM REMOTE!HELLO FROM REMOTE!, world!!

```

## Logging

```text
INFO	ordeq.io	Loading StringBuffer(_buffer=<_io.StringIO object at HASH1>)
INFO	ordeq.runner	Running node "uppercase" in module "run_io_catalog_reference"
INFO	ordeq.io	Saving StringBuffer(_buffer=<_io.StringIO object at HASH2>)
INFO	ordeq.runner	Running node "add_world" in module "run_io_catalog_reference"
INFO	ordeq.io	Saving Print()
INFO	ordeq.io	Loading StringBuffer(_buffer=<_io.StringIO object at HASH1>)
INFO	ordeq.runner	Running node "uppercase" in module "run_io_catalog_reference"
INFO	ordeq.io	Saving StringBuffer(_buffer=<_io.StringIO object at HASH2>)
INFO	ordeq.runner	Running node "add_world" in module "run_io_catalog_reference"
INFO	ordeq.io	Saving Print()
INFO	ordeq.io	Loading StringBuffer(_buffer=<_io.StringIO object at HASH1>)
INFO	ordeq.runner	Running node "uppercase" in module "run_io_catalog_reference"
INFO	ordeq.io	Saving StringBuffer(_buffer=<_io.StringIO object at HASH2>)
INFO	ordeq.runner	Running node "add_world" in module "run_io_catalog_reference"
INFO	ordeq.io	Saving Print()

```