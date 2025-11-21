## Resource

```python
from ordeq import node, run
from ordeq._nodes import get_node
from ordeq_common import Literal, Print


@node
def hello() -> str:
    return "Hello, World!"


print(repr(get_node(hello)))


@node(inputs=[Literal("Jane"), hello], outputs=Print())
def n(name: str, greeting: str) -> str:
    return f"{name} said '{greeting}'"


run(n, verbose=True)

```

## Output

```text
View(func=<function hello at HASH1>)
View:__main__:hello --> io-0
io-0 --> Node:__main__:n
io-1 --> Node:__main__:n
Node:__main__:n --> io-2
Jane said 'Hello, World!'

```

## Logging

```text
INFO	ordeq.runner	Running view "hello" in module "__main__"
INFO	ordeq.io	Loading Literal('Jane')
INFO	ordeq.runner	Running node "n" in module "__main__"
INFO	ordeq.io	Saving Print()

```