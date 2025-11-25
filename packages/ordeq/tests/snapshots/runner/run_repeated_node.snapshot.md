## Resource

```python
from ordeq import node, run
from ordeq_common import StringBuffer

x = StringBuffer()


@node(outputs=x)
def func1() -> str:
    return "Hello"


run(func1, func1)

```

## Warnings

```text
UserWarning: 'func1' in module '__main__' was provided more than once. Duplicates are ignored.
UserWarning: 'func1' in module '__main__' was provided more than once. Duplicates are ignored.
```

## Logging

```text
INFO	ordeq.runner	Running node 'func1' in module '__main__'
INFO	ordeq.io	Saving StringBuffer(_buffer=<_io.StringIO object at HASH1>)
DEBUG	ordeq.io	Persisting data for StringBuffer(_buffer=<_io.StringIO object at HASH1>)
DEBUG	ordeq.io	Unpersisting data for StringBuffer(_buffer=<_io.StringIO object at HASH1>)

```