## Resource

```python
from ordeq import node, run
from ordeq._nodes import get_node
from ordeq_common import Print


@node
def hello() -> str:
    return "Hello, World!"


print(repr(get_node(hello)))


@node(inputs=hello, outputs=Print())
def n(greeting: str) -> str:
    return f"She said '{greeting}'"


run(n, verbose=True)

```

## Output

```text
View(name=__main__:hello)
View:__main__:hello --> io-0
io-0 --> Node:__main__:n
Node:__main__:n --> io-1
She said 'Hello, World!'

```

## Logging

```text
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node '__main__:hello'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
INFO	ordeq.runner	Running view "hello" in module "__main__"
INFO	ordeq.runner	Running node "n" in module "__main__"
INFO	ordeq.io	Saving Print()

```