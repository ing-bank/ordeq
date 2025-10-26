## Resource

```python
from ordeq import node, run
from ordeq_common import StringBuffer

x = StringBuffer()


@node(outputs=x)
def func1() -> str:
    return "Hello"


@node(outputs=x)
def func2() -> str:
    return "world"


run(func1, func2, verbose=True)

```

## Output

```text
NodeGraph:
  Edges:
     runner_non_distinct_ios:func1 -> []
     runner_non_distinct_ios:func2 -> []
  Nodes:
     Node(name=runner_non_distinct_ios:func1, outputs=[StringBuffer(_buffer=<_io.StringIO object at HASH1>)])
     Node(name=runner_non_distinct_ios:func2, outputs=[StringBuffer(_buffer=<_io.StringIO object at HASH1>)])

```

## Logging

```text
INFO	ordeq.runner	Running node Node(name=runner_non_distinct_ios:func2, outputs=[StringBuffer(_buffer=<_io.StringIO object at HASH1>)])
INFO	ordeq.io	Saving StringBuffer(_buffer=<_io.StringIO object at HASH1>)
INFO	ordeq.runner	Running node Node(name=runner_non_distinct_ios:func1, outputs=[StringBuffer(_buffer=<_io.StringIO object at HASH1>)])
INFO	ordeq.io	Saving StringBuffer(_buffer=<_io.StringIO object at HASH1>)

```