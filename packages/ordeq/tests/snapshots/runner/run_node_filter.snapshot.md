## Resource

```python
from ordeq import Node, node, run
from ordeq_common import Literal, StringBuffer

greeting = Literal("Hello")
buffer = StringBuffer()


@node(inputs=greeting, outputs=buffer)
def hello(hi: str) -> str:
    print("Saying", hi)
    return hi


@node(inputs=buffer)
def world(value: str) -> str:
    say = f"{value}, world!!"
    print("Saying", say)
    return say


def takes_greeting(n: Node) -> bool:
    return greeting in n.inputs


print("Should run only `hello` (filter returns False for `world`):")
run(hello, world, node_filter=takes_greeting)

```

## Output

```text
Should run only `hello` (filter returns False for `world`):
Saying Hello

```

## Logging

```text
WARNING	ordeq.preview	Node filters are in preview mode and may change without notice in future releases.
INFO	ordeq.io	Loading Literal('Hello')
DEBUG	ordeq.io	Persisting data for Literal('Hello')
INFO	ordeq.runner	Running node 'hello' in module '__main__'
INFO	ordeq.io	Saving StringBuffer(_buffer=<_io.StringIO object at HASH1>)
DEBUG	ordeq.io	Persisting data for StringBuffer(_buffer=<_io.StringIO object at HASH1>)
DEBUG	ordeq.io	Unpersisting data for Literal('Hello')
DEBUG	ordeq.io	Unpersisting data for StringBuffer(_buffer=<_io.StringIO object at HASH1>)

```