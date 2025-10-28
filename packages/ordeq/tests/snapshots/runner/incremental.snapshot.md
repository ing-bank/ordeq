## Resource

```python
from ordeq import node
from ordeq._runner import run
from ordeq_common import StringBuffer

I1 = StringBuffer("Hello")
I2 = StringBuffer("world!")


def f1(i: str, j: str) -> str:
    return f"{i} {j}"


def c():
    a = I1.load()
    b = I2.load()
    return f1(a, b)


print(c())

print(node(c, outputs=StringBuffer("result"))())

output = StringBuffer("result")
print(run(node(c, outputs=output))[output])

```

## Output

```text
Hello world!
Hello world!
Hello world!

```

## Logging

```text
INFO	ordeq.io	Loading StringBuffer(_buffer=<_io.StringIO object at HASH1>)
INFO	ordeq.io	Loading StringBuffer(_buffer=<_io.StringIO object at HASH2>)
INFO	ordeq.io	Loading StringBuffer(_buffer=<_io.StringIO object at HASH1>)
INFO	ordeq.io	Loading StringBuffer(_buffer=<_io.StringIO object at HASH2>)
INFO	ordeq.runner	Running node "c" in module "incremental"
INFO	ordeq.io	Loading StringBuffer(_buffer=<_io.StringIO object at HASH1>)
INFO	ordeq.io	Loading StringBuffer(_buffer=<_io.StringIO object at HASH2>)
INFO	ordeq.io	Saving StringBuffer(_buffer=<_io.StringIO object at HASH3>)

```