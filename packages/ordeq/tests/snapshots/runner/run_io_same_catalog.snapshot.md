## Resource

```python
# Checks the behaviour when running nodes with an alternative catalog
# We want to support this syntax and behaviour since it allows users to
# easily switch between different catalogs, for instance during tests.
from example_catalogs import remote
from ordeq import node, run
from ordeq_common import Print

catalog = remote


@node(inputs=catalog.hello, outputs=catalog.result)
def uppercase(hello: str) -> str:
    return f"{hello.upper()}!"


@node(inputs=catalog.result, outputs=Print())
def add_world(hello: str) -> str:
    return f"{hello}, world!!"


run(uppercase, add_world, io={catalog: catalog})

```

## Output

```text
HELLO FROM REMOTE!HEY I AM OVERRIDING THE HELLO IO!HELLO FROM REMOTE!HELLO FROM REMOTE!HELLO FROM REMOTE!HEY I AM OVERRIDING THE HELLO IO!HELLO FROM REMOTE!HELLO FROM REMOTE!HELLO FROM REMOTE!HEY I AM OVERRIDING THE HELLO IO!HELLO FROM REMOTE!, world!!

```

## Logging

```text
INFO	ordeq.runner	Loading StringBuffer 'uppercase:hello' in module '__main__'
DEBUG	ordeq.io	Persisting data for StringBuffer 'uppercase:hello' in module '__main__'
INFO	ordeq.runner	Running node 'uppercase' in module '__main__'
INFO	ordeq.runner	Saving StringBuffer 'add_world:hello' in module '__main__'
DEBUG	ordeq.io	Persisting data for StringBuffer 'add_world:hello' in module '__main__'
INFO	ordeq.runner	Loading StringBuffer 'add_world:hello' in module '__main__'
DEBUG	ordeq.io	Loading cached data for StringBuffer 'add_world:hello' in module '__main__'
INFO	ordeq.runner	Running node 'add_world' in module '__main__'
INFO	ordeq.runner	Saving Print()
DEBUG	ordeq.io	Unpersisting data for StringBuffer 'uppercase:hello' in module '__main__'
DEBUG	ordeq.io	Unpersisting data for StringBuffer 'add_world:hello' in module '__main__'

```