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
io-0 --> Node:__main__:increment
io-0 --> Node:__main__:decrement
Node:__main__:increment --> io-1
io-1 --> Node:__main__:decrement
Node:__main__:decrement --> io-2
1
io-0 --> Node:__main__:increment
io-0 --> Node:__main__:decrement
Node:__main__:increment --> io-1
io-1 --> Node:__main__:decrement
Node:__main__:decrement --> io-2
12001

```

## Logging

```text
INFO	ordeq.io	Loading Literal(1)
INFO	ordeq.runner	Running node '__main__:increment'
INFO	ordeq.io	Saving StringBuffer(_buffer=<_io.StringIO object at HASH1>)
INFO	ordeq.runner	Running node '__main__:decrement'
INFO	ordeq.io	Saving StringBuffer(_buffer=<_io.StringIO object at HASH2>)
INFO	ordeq.io	Loading StringBuffer(_buffer=<_io.StringIO object at HASH2>)
INFO	ordeq.io	Loading Literal(200)
INFO	ordeq.runner	Running node '__main__:increment'
INFO	ordeq.io	Saving StringBuffer(_buffer=<_io.StringIO object at HASH1>)
INFO	ordeq.runner	Running node '__main__:decrement'
INFO	ordeq.io	Saving StringBuffer(_buffer=<_io.StringIO object at HASH2>)
INFO	ordeq.io	Loading StringBuffer(_buffer=<_io.StringIO object at HASH2>)

```