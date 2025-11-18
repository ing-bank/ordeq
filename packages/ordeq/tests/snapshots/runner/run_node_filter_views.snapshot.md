## Resource

```python
from ordeq import Node, node, run
from ordeq_common import Literal, Print

greeting = Literal("Hello")


@node(inputs=greeting, prints=False)
def hello(hi: str) -> str:
    return hi


@node(inputs=hello, outputs=Print(), prints=True)
def world(value: str) -> str:
    say = f"{value}, world!!"
    print("Saying", say)
    return say


def prints(n: Node) -> bool:
    return n.attributes.get("prints", False)


print("Should run both `hello` and `world`:")
# Even though the filter only returns True for `world`, `hello` is a view
# and is run because `world` is run.
run(hello, world, node_filter=prints, verbose=True)

print("Should run neither `hello` nor `world`:")
run(hello, node_filter=prints, verbose=True)

print("Should run both `hello` and `world`:")
run(world, node_filter=prints, verbose=True)

```

## Output

```text
Should run both `hello` and `world`:
io-0 --> View:__main__:hello
View:__main__:hello --> io-1
io-1 --> Node:__main__:world
Node:__main__:world --> io-2
Saying Hello, world!!
Hello, world!!
Should run neither `hello` nor `world`:

Should run both `hello` and `world`:
io-0 --> View:__main__:hello
View:__main__:hello --> io-1
io-1 --> Node:__main__:world
Node:__main__:world --> io-2
Saying Hello, world!!
Hello, world!!

```

## Logging

```text
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node '__main__:hello'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.runner	Node filters are in preview mode and may change without notice in future releases.
INFO	ordeq.io	Loading Literal('Hello')
INFO	ordeq.runner	Running view "hello" in module "__main__"
INFO	ordeq.runner	Running node "world" in module "__main__"
INFO	ordeq.io	Saving Print()
WARNING	ordeq.runner	Node filters are in preview mode and may change without notice in future releases.
WARNING	ordeq.runner	Node filters are in preview mode and may change without notice in future releases.
INFO	ordeq.io	Loading Literal('Hello')
INFO	ordeq.runner	Running view "hello" in module "__main__"
INFO	ordeq.runner	Running node "world" in module "__main__"
INFO	ordeq.io	Saving Print()

```