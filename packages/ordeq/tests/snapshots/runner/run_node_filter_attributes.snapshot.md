## Resource

```python
from ordeq import Node, node, run
from ordeq_common import Literal, StringBuffer

greeting = Literal("Hello")
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
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node '__main__:world'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq._process_nodes	Node filters are in preview mode and may change without notice in future releases.
INFO	ordeq.io	Loading StringBuffer(_buffer=<_io.StringIO object at HASH1>)
INFO	ordeq.runner	Running view "world" in module "__main__"

```