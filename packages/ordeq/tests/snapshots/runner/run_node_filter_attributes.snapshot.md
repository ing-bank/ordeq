## Resource

```python
from ordeq import Input, Node, node, run
from ordeq_common import StringBuffer

greeting = Input[str]("Hello")
buffer = StringBuffer()


@node(inputs=greeting, outputs=buffer)
def hello(hi: str) -> str:
    return hi


@node(inputs=buffer, prints=True)
def world(value: str) -> str:
    say = f"{value}, world!!"
    print("Saying", say)
    return say


def prints(n: Node) -> bool:
    return n.attributes.get("prints", False)


print("Should run only `world` (filter returns False for `hello`):")
run(hello, world, node_filter=prints)

```

## Output

```text
Should run only `world` (filter returns False for `hello`):
Saying , world!!

```

## Logging

```text
DEBUG	ordeq.io	Persisting data for Input(id=ID1)
WARNING	ordeq.preview	Node filters are in preview mode and may change without notice in future releases.
DEBUG	ordeq.runner	Running StringBuffer(_buffer=<_io.StringIO object at HASH1>)
INFO	ordeq.io	Loading StringBuffer(_buffer=<_io.StringIO object at HASH1>)
DEBUG	ordeq.io	Persisting data for IO 'world:value' in module '__main__'
DEBUG	ordeq.io	Loading cached data for IO 'world:value' in module '__main__'
DEBUG	ordeq.runner	Running view 'world' in module '__main__'
DEBUG	ordeq.io	Persisting data for IO(id=ID2)
DEBUG	ordeq.io	Unpersisting data for IO 'world:value' in module '__main__'
DEBUG	ordeq.io	Unpersisting data for IO(id=ID2)

```