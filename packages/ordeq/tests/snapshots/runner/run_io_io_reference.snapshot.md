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

```

## Output

```text
HELLO FROM REMOTE!, world!!
HELLO FROM REMOTE!HELLO FROM REMOTE!, world!!
HELLO FROM REMOTE!HELLO FROM REMOTE!HELLO FROM REMOTE!, world!!

```

## Logging

```text
INFO	ordeq.io	Loading StringBuffer(_buffer=<_io.StringIO object at HASH1>)
INFO	ordeq.runner	Running node "uppercase" in module "run_io_io_reference"
INFO	ordeq.io	Saving StringBuffer(_buffer=<_io.StringIO object at HASH2>)
INFO	ordeq.runner	Running node "add_world" in module "run_io_io_reference"
INFO	ordeq.io	Saving Print()
INFO	ordeq.runner	Running node "uppercase" in module "run_io_io_reference"
INFO	ordeq.io	Saving StringBuffer(_buffer=<_io.StringIO object at HASH2>)
INFO	ordeq.runner	Running node "add_world" in module "run_io_io_reference"
INFO	ordeq.io	Saving Print()
INFO	ordeq.runner	Running node "uppercase" in module "run_io_io_reference"
INFO	ordeq.io	Saving StringBuffer(_buffer=<_io.StringIO object at HASH2>)
INFO	ordeq.runner	Running node "add_world" in module "run_io_io_reference"
INFO	ordeq.io	Saving Print()

```