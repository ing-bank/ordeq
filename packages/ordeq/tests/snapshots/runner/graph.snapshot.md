## Resource

```python
from ordeq import node
from ordeq._runner import run
from ordeq_common import StringBuffer

I1 = StringBuffer("Hello")
I2 = StringBuffer("world!")
R1 = StringBuffer()
R2 = StringBuffer()
R3 = StringBuffer()
R4 = StringBuffer()


@node(inputs=[I1, I2], outputs=[R1])
def f1(i: str, j: str) -> str:
    return f"{i} + {j}"


@node(inputs=[I2, R1], outputs=[R2])
def f2(i: str, j: str) -> str:
    return f"{i} - {j}"


@node(inputs=[R1], outputs=[R3])
def f3(i: str) -> str:
    return f"{i} * 2"


@node(inputs=[R1, R2, R3], outputs=[R4])
def f4(i: str, j: str, k: str) -> str:
    return f"{i} / {j} + {k}"


pipeline = [f1, f2, f3, f4]

run(*pipeline, save="all", verbose=True)
print(R4.load())

run(*pipeline, save="sinks", verbose=True)
print(R4.load())

run(*pipeline, save="none", verbose=True)
print(R4.load())

```

## Output

```text
io-0 --> Node:__main__:f1
io-0 --> Node:__main__:f2
io-1 --> Node:__main__:f1
Node:__main__:f1 --> io-2
io-2 --> Node:__main__:f3
io-2 --> Node:__main__:f2
io-2 --> Node:__main__:f4
Node:__main__:f3 --> io-3
Node:__main__:f2 --> io-4
io-3 --> Node:__main__:f4
io-4 --> Node:__main__:f4
Node:__main__:f4 --> io-5
Hello + world! / world! - Hello + world! + Hello + world! * 2
io-0 --> Node:__main__:f1
io-0 --> Node:__main__:f2
io-1 --> Node:__main__:f1
Node:__main__:f1 --> io-2
io-2 --> Node:__main__:f3
io-2 --> Node:__main__:f2
io-2 --> Node:__main__:f4
Node:__main__:f3 --> io-3
Node:__main__:f2 --> io-4
io-3 --> Node:__main__:f4
io-4 --> Node:__main__:f4
Node:__main__:f4 --> io-5
Hello + world! / world! - Hello + world! + Hello + world! * 2Hello + world! / world! - Hello + world! + Hello + world! * 2
io-0 --> Node:__main__:f1
io-0 --> Node:__main__:f2
io-1 --> Node:__main__:f1
Node:__main__:f1 --> io-2
io-2 --> Node:__main__:f3
io-2 --> Node:__main__:f2
io-2 --> Node:__main__:f4
Node:__main__:f3 --> io-3
Node:__main__:f2 --> io-4
io-3 --> Node:__main__:f4
io-4 --> Node:__main__:f4
Node:__main__:f4 --> io-5
Hello + world! / world! - Hello + world! + Hello + world! * 2Hello + world! / world! - Hello + world! + Hello + world! * 2

```

## Logging

```text
INFO	ordeq.io	Loading StringBuffer(_buffer=<_io.StringIO object at HASH1>)
INFO	ordeq.io	Loading StringBuffer(_buffer=<_io.StringIO object at HASH2>)
INFO	ordeq.runner	Running node "f1" in module "__main__"
INFO	ordeq.io	Saving StringBuffer(_buffer=<_io.StringIO object at HASH3>)
INFO	ordeq.runner	Running node "f3" in module "__main__"
INFO	ordeq.io	Saving StringBuffer(_buffer=<_io.StringIO object at HASH4>)
INFO	ordeq.runner	Running node "f2" in module "__main__"
INFO	ordeq.io	Saving StringBuffer(_buffer=<_io.StringIO object at HASH5>)
INFO	ordeq.runner	Running node "f4" in module "__main__"
INFO	ordeq.io	Saving StringBuffer(_buffer=<_io.StringIO object at HASH6>)
INFO	ordeq.io	Loading StringBuffer(_buffer=<_io.StringIO object at HASH6>)
INFO	ordeq.io	Loading StringBuffer(_buffer=<_io.StringIO object at HASH1>)
INFO	ordeq.io	Loading StringBuffer(_buffer=<_io.StringIO object at HASH2>)
INFO	ordeq.runner	Running node "f1" in module "__main__"
INFO	ordeq.runner	Running node "f3" in module "__main__"
INFO	ordeq.runner	Running node "f2" in module "__main__"
INFO	ordeq.runner	Running node "f4" in module "__main__"
INFO	ordeq.io	Saving StringBuffer(_buffer=<_io.StringIO object at HASH6>)
INFO	ordeq.io	Loading StringBuffer(_buffer=<_io.StringIO object at HASH6>)
INFO	ordeq.io	Loading StringBuffer(_buffer=<_io.StringIO object at HASH1>)
INFO	ordeq.io	Loading StringBuffer(_buffer=<_io.StringIO object at HASH2>)
INFO	ordeq.runner	Running node "f1" in module "__main__"
INFO	ordeq.runner	Running node "f3" in module "__main__"
INFO	ordeq.runner	Running node "f2" in module "__main__"
INFO	ordeq.runner	Running node "f4" in module "__main__"
INFO	ordeq.io	Loading StringBuffer(_buffer=<_io.StringIO object at HASH6>)

```