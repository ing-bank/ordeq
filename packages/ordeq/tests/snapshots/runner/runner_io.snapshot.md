## Resource

```python
from ordeq import node
from ordeq._runner import run
from ordeq_common import Literal, StringBuffer

x1 = Literal(1)
x2 = StringBuffer()
x3 = StringBuffer("2")
x4 = StringBuffer()


@node(inputs=x1, outputs=x2)
def increment(x: int) -> str:
    return f"{x + 1}"


@node(inputs=[x2, x3], outputs=x4)
def decrement(x: str, y: str) -> str:
    return f"{int(x) - int(y)}"


run(increment, decrement, verbose=True)

print(x4.load())

# provide alternative IO when running the pipeline
p1 = Literal(2)
p3 = Literal("33")
p4 = StringBuffer()
run(increment, decrement, io={x1: p1, x3: p3, x4: p4}, verbose=True)

print(p4.load())

```

## Output

```text
Node:runner_io:decrement --> io-1
Node:runner_io:increment --> io-2
io-2 --> Node:runner_io:decrement
0
Node:runner_io:decrement --> io-1
Node:runner_io:increment --> io-2
io-2 --> Node:runner_io:decrement
-10

```

## Logging

```text
INFO	ordeq.io	Loading Literal(1)
INFO	ordeq.runner	Running node "increment" in module "runner_io"
INFO	ordeq.io	Saving StringBuffer(_buffer=<_io.StringIO object at HASH1>)
INFO	ordeq.io	Loading StringBuffer(_buffer=<_io.StringIO object at HASH2>)
INFO	ordeq.runner	Running node "decrement" in module "runner_io"
INFO	ordeq.io	Saving StringBuffer(_buffer=<_io.StringIO object at HASH3>)
INFO	ordeq.io	Loading StringBuffer(_buffer=<_io.StringIO object at HASH3>)
INFO	ordeq.io	Loading Literal(2)
INFO	ordeq.runner	Running node "increment" in module "runner_io"
INFO	ordeq.io	Saving StringBuffer(_buffer=<_io.StringIO object at HASH1>)
INFO	ordeq.io	Loading Literal('33')
INFO	ordeq.runner	Running node "decrement" in module "runner_io"
INFO	ordeq.io	Saving StringBuffer(_buffer=<_io.StringIO object at HASH4>)
INFO	ordeq.io	Loading StringBuffer(_buffer=<_io.StringIO object at HASH4>)

```