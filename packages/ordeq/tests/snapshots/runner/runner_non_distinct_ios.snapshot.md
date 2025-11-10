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
<ordeq._graph.NodeIOGraph object at HASH1>

```

## Logging

```text
INFO	ordeq.runner	Running node "func2" in module "runner_non_distinct_ios"
INFO	ordeq.io	Saving StringBuffer(_buffer=<_io.StringIO object at HASH2>)
INFO	ordeq.runner	Running node "func1" in module "runner_non_distinct_ios"
INFO	ordeq.io	Saving StringBuffer(_buffer=<_io.StringIO object at HASH2>)

```