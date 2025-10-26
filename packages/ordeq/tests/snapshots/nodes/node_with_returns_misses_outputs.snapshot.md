## Resource

```python
from ordeq import node, run
from ordeq_common import StringBuffer


@node(inputs=[StringBuffer("a")])
def func(x: str) -> str:
    return x


run(func)

```

## Exception

```text
CycleError: ('nodes are in a cycle', [View(name=node_with_returns_misses_outputs:func, inputs=[StringBuffer(_buffer=<_io.StringIO object at HASH1>)]), View(name=node_with_returns_misses_outputs:func, inputs=[StringBuffer(_buffer=<_io.StringIO object at HASH1>)])])
```

## Logging

```text
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'node_with_returns_misses_outputs:func'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 

```