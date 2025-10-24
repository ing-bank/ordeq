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
NodeGraph:
  Edges:
     runner_distinct_ios:func1 -> []
     runner_distinct_ios:func2 -> []
  Nodes:
     Node(name=runner_distinct_ios:func1, outputs=[StringBuffer(_buffer=<_io.StringIO object at HASH1>)])
     Node(name=runner_distinct_ios:func2, outputs=[StringBuffer(_buffer=<_io.StringIO object at HASH2>)])

```

## Logging

```text
INFO	ordeq.runner	Running node Node(name=runner_distinct_ios:func2, outputs=[StringBuffer(_buffer=<_io.StringIO object at HASH2>)])
INFO	ordeq.io	Saving StringBuffer(_buffer=<_io.StringIO object at HASH2>)
INFO	ordeq.runner	Running node Node(name=runner_distinct_ios:func1, outputs=[StringBuffer(_buffer=<_io.StringIO object at HASH1>)])
INFO	ordeq.io	Saving StringBuffer(_buffer=<_io.StringIO object at HASH1>)

```