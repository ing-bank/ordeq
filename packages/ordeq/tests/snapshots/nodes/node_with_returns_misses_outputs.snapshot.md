## Resource

```python
from ordeq import node, run
from ordeq_common import StringBuffer


@node(inputs=[StringBuffer("a")])
def func(x: str) -> str:
    return x


run(func)

```

## Logging

```text
DEBUG	ordeq.runner	Running StringBuffer(_buffer=<_io.StringIO object at HASH1>)
INFO	ordeq.io	Loading StringBuffer(_buffer=<_io.StringIO object at HASH1>)
DEBUG	ordeq.io	Persisting data for IO 'func:x' in module '__main__'
DEBUG	ordeq.io	Loading cached data for IO 'func:x' in module '__main__'
DEBUG	ordeq.runner	Running view 'func' in module '__main__'
DEBUG	ordeq.io	Persisting data for IO(id=ID1)
DEBUG	ordeq.io	Unpersisting data for IO 'func:x' in module '__main__'
DEBUG	ordeq.io	Unpersisting data for IO(id=ID1)

```