## Resource

```python
from ordeq import node, run
from ordeq_common import Literal, StringBuffer

greeting = Literal("Hello")
buffer = StringBuffer()


@node(inputs=greeting, outputs=buffer)
def hello(hi: str) -> str:
    print("Saying", hi)
    return hi


@node(inputs=buffer)
def world(value: str) -> str:
    say = f"{value}, world!"
    print("Saying", say)
    return say


print("Should run all nodes (node filter maps all nodes to True):")
run(hello, world, node_filter=lambda n: True)

print("Should run no nodes (node filter maps all nodes to False):")
run(hello, world, node_filter=lambda n: False)

```

## Output

```text
Should run all nodes (node filter maps all nodes to True):
Saying Hello
Saying Hello, world!
Should run no nodes (node filter maps all nodes to False):

```

## Logging

```text
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node '__main__:world'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.runner	Node filters are in preview mode and may change without notice in future releases.
INFO	ordeq.io	Loading Literal('Hello')
INFO	ordeq.runner	Running node "hello" in module "__main__"
INFO	ordeq.io	Saving StringBuffer(_buffer=<_io.StringIO object at HASH1>)
INFO	ordeq.runner	Running view "world" in module "__main__"
WARNING	ordeq.runner	Node filters are in preview mode and may change without notice in future releases.

```