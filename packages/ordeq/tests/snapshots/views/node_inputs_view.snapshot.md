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
View(func=<function hello at HASH1>)
View:__main__:hello --> io-0
io-0 --> Node:__main__:n
Node:__main__:n --> io-1
She said 'Hello, World!'

```

## Logging

```text
INFO	ordeq.runner	Running view "hello" in module "__main__"
INFO	ordeq.runner	Running node "n" in module "__main__"
INFO	ordeq.io	Saving Print()

```