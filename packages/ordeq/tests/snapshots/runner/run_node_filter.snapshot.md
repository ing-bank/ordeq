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
WARNING	ordeq.preview	Creating a view, as no outputs were provided for node '__main__:world'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.preview	Node filters are in preview mode and may change without notice in future releases.
INFO	ordeq.io	Loading Literal('Hello')
INFO	ordeq.runner	Running node "hello" in module "__main__"
INFO	ordeq.io	Saving StringBuffer(_buffer=<_io.StringIO object at HASH1>)

```