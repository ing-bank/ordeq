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
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node '__main__:func'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
INFO	ordeq.io	Loading StringBuffer(_buffer=<_io.StringIO object at HASH1>)
INFO	ordeq.runner	Running view "func" in module "__main__"

```