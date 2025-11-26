## Resource

```python
from example_catalogs import remote_extended
from ordeq import node, run

catalog = remote_extended


@node(inputs=catalog.hello, outputs=catalog.another_io)
def func1(hello: str) -> str:
    return f"{hello.upper()}!"


run(func1)  # 'catalog.another_io' prints the output to stdout

```

## Output

```text
HELLO FROM REMOTE!

```

## Logging

```text
INFO	ordeq.io	Loading StringBuffer(_buffer=<_io.StringIO object at HASH1>)
DEBUG	ordeq.io	Persisting data for StringBuffer(_buffer=<_io.StringIO object at HASH1>)
INFO	ordeq.runner	Running node 'func1' in module '__main__'
INFO	ordeq.io	Saving Print()
DEBUG	ordeq.io	Unpersisting data for StringBuffer(_buffer=<_io.StringIO object at HASH1>)

```