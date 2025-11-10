## Resource

```python
from ordeq import node
from ordeq._runner import run
from ordeq_common import Literal, StringBuffer

x1 = Literal(1)
x2 = StringBuffer()
x3 = StringBuffer()


@node(inputs=x1, outputs=x2)
def increment(x: int) -> str:
    return f"{x + 1}"


@node(inputs=[x2, x1], outputs=x3)
def decrement(x: str, y: str) -> str:
    return f"{int(x) - int(y)}"


run(increment, decrement, verbose=True)

print(x3.load())

# provide alternative IO when running the pipeline
p1 = Literal(200)
run(increment, decrement, io={x1: p1}, verbose=True)

print(x3.load())

```

## Output

```text
<ordeq._graph.NodeIOGraph object at HASH1>
1
<ordeq._graph.NodeIOGraph object at HASH2>
12001

```

## Logging

```text
INFO	ordeq.io	Loading Literal(1)
INFO	ordeq.runner	Running node "increment" in module "runner_io_more_than_once"
INFO	ordeq.io	Saving StringBuffer(_buffer=<_io.StringIO object at HASH3>)
INFO	ordeq.runner	Running node "decrement" in module "runner_io_more_than_once"
INFO	ordeq.io	Saving StringBuffer(_buffer=<_io.StringIO object at HASH4>)
INFO	ordeq.io	Loading StringBuffer(_buffer=<_io.StringIO object at HASH4>)
INFO	ordeq.io	Loading Literal(200)
INFO	ordeq.runner	Running node "increment" in module "runner_io_more_than_once"
INFO	ordeq.io	Saving StringBuffer(_buffer=<_io.StringIO object at HASH3>)
INFO	ordeq.runner	Running node "decrement" in module "runner_io_more_than_once"
INFO	ordeq.io	Saving StringBuffer(_buffer=<_io.StringIO object at HASH4>)
INFO	ordeq.io	Loading StringBuffer(_buffer=<_io.StringIO object at HASH4>)

```