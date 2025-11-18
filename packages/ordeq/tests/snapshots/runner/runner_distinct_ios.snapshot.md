## Resource

```python
from ordeq import node, run
from ordeq_common import StringBuffer


@node(outputs=StringBuffer())
def func1() -> str:
    return "Hello"


@node(outputs=StringBuffer())
def func2() -> str:
    return "world"


run(func1, func2, verbose=True)

```

## Output

```text
NodeResourceGraph(nodes=2, resources=2, edges={Node(name=__main__:func2, outputs=[StringBuffer(_buffer=<_io.StringIO object at HASH1>)]): [Resource(value=StringBuffer(_buffer=<_io.StringIO object at HASH1>))], Node(name=__main__:func1, outputs=[StringBuffer(_buffer=<_io.StringIO object at HASH2>)]): [Resource(value=StringBuffer(_buffer=<_io.StringIO object at HASH2>))], Resource(value=StringBuffer(_buffer=<_io.StringIO object at HASH1>)): [], Resource(value=StringBuffer(_buffer=<_io.StringIO object at HASH2>)): []})

```

## Logging

```text
INFO	ordeq.runner	Running node "func1" in module "__main__"
INFO	ordeq.io	Saving StringBuffer(_buffer=<_io.StringIO object at HASH2>)
INFO	ordeq.runner	Running node "func2" in module "__main__"
INFO	ordeq.io	Saving StringBuffer(_buffer=<_io.StringIO object at HASH1>)

```