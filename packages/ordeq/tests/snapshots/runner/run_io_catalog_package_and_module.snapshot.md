## Resource

```python
# Checks the behaviour when running nodes with an alternative catalog
# We want to support this syntax and behaviour since it allows users to
# easily switch between different catalogs, for instance during tests.
from example_catalogs import (
    local,
    local_package,
    remote_extended,
    remote_package,
)
from ordeq import node, run
from ordeq_common import Print

catalog = local_package


@node(inputs=local_package.hello, outputs=remote_extended.result)
def uppercase(hello: str) -> str:
    return f"{hello.upper()}!"


@node(inputs=local_package.result, outputs=Print())
def add_world(hello: str) -> str:
    return f"{hello}, world!!"


run(
    uppercase,
    add_world,
    io={local_package: remote_package, remote_extended: local},
)

```

## Output

```text
HELLO FROM REMOTE!, world!!

```

## Logging

```text
INFO	ordeq.io	Loading StringBuffer(_buffer=<_io.StringIO object at HASH1>)
DEBUG	ordeq.io	Persisting data for StringBuffer(_buffer=<_io.StringIO object at HASH1>)
INFO	ordeq.runner	Running node 'uppercase' in module '__main__'
INFO	ordeq.io	Saving StringBuffer 'add_world:hello' in module '__main__'
DEBUG	ordeq.io	Persisting data for StringBuffer 'add_world:hello' in module '__main__'
INFO	ordeq.io	Loading StringBuffer(_buffer=<_io.StringIO object at HASH2>)
DEBUG	ordeq.io	Persisting data for StringBuffer(_buffer=<_io.StringIO object at HASH2>)
INFO	ordeq.runner	Running node 'add_world' in module '__main__'
INFO	ordeq.io	Saving Print()
DEBUG	ordeq.io	Unpersisting data for StringBuffer(_buffer=<_io.StringIO object at HASH2>)
DEBUG	ordeq.io	Unpersisting data for StringBuffer(_buffer=<_io.StringIO object at HASH1>)
DEBUG	ordeq.io	Unpersisting data for StringBuffer 'add_world:hello' in module '__main__'

```