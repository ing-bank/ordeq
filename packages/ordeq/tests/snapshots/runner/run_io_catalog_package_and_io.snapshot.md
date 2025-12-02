## Resource

```python
# Checks the behaviour when running nodes with an alternative catalog
# We want to support this syntax and behaviour since it allows users to
# easily switch between different catalogs, for instance during tests.
from example_catalogs import remote, remote_overridden
from ordeq import node, run
from ordeq_common import Print, StringBuffer

catalog = remote


@node(inputs=catalog.hello, outputs=catalog.result)
def uppercase(hello: str) -> str:
    return f"{hello.upper()}!"


@node(inputs=catalog.result, outputs=Print())
def add_world(hello: str) -> str:
    return f"{hello}, world!!"


run(
    uppercase,
    add_world,
    io={
        catalog: remote_overridden,
        catalog.result: StringBuffer("I want to say: "),
    },
)

```

## Output

```text
HELLO FROM REMOTE!HEY I AM OVERRIDING THE HELLO IO!HELLO FROM REMOTE!HELLO FROM LOCAL!HELLO FROM REMOTE!HELLO FROM REMOTE!, world!!

```

## Logging

```text
DEBUG	ordeq.runner	Running StringBuffer(_buffer=<_io.StringIO object at HASH1>)
INFO	ordeq.io	Loading StringBuffer(_buffer=<_io.StringIO object at HASH1>)
DEBUG	ordeq.io	Persisting data for IO 'uppercase:hello' in module '__main__'
DEBUG	ordeq.runner	Running StringBuffer(_buffer=<_io.StringIO object at HASH2>)
INFO	ordeq.io	Loading StringBuffer(_buffer=<_io.StringIO object at HASH2>)
DEBUG	ordeq.io	Persisting data for IO 'add_world:hello' in module '__main__'
DEBUG	ordeq.io	Loading cached data for IO 'uppercase:hello' in module '__main__'
DEBUG	ordeq.runner	Running node 'uppercase' in module '__main__'
INFO	ordeq.io	Saving StringBuffer(_buffer=<_io.StringIO object at HASH3>)
DEBUG	ordeq.io	Persisting data for StringBuffer(_buffer=<_io.StringIO object at HASH3>)
DEBUG	ordeq.io	Loading cached data for IO 'add_world:hello' in module '__main__'
DEBUG	ordeq.runner	Running node 'add_world' in module '__main__'
INFO	ordeq.io	Saving Print()
DEBUG	ordeq.io	Unpersisting data for IO 'add_world:hello' in module '__main__'
DEBUG	ordeq.io	Unpersisting data for IO 'uppercase:hello' in module '__main__'
DEBUG	ordeq.io	Unpersisting data for StringBuffer(_buffer=<_io.StringIO object at HASH3>)

```