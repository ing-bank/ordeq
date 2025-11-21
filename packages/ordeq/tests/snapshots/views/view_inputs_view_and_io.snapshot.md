## Resource

```python
from ordeq import node, run
from ordeq._nodes import get_node
from ordeq_common import Literal


@node
def hello() -> str:
    return "Hello, World!"


print(repr(get_node(hello)))


@node(inputs=[Literal("Jane"), hello])
def hello_from_someone(name: str, v: str) -> str:
    return f"{name} said '{v}'"


print(repr(get_node(hello_from_someone)))


@node(inputs=hello_from_someone)
def n(v: str) -> None:
    print(f"I heard that {v}")


run(n, verbose=True)

```

## Output

```text
View(func=<function hello at HASH1>)
View(func=<function hello_from_someone at HASH2>, inputs=[Literal('Jane'), IO(id=ID1)])
View:__main__:hello --> io-0
io-0 --> View:__main__:hello_from_someone
io-1 --> View:__main__:hello_from_someone
View:__main__:hello_from_someone --> io-2
io-2 --> View:__main__:n
View:__main__:n --> io-3
I heard that Jane said 'Hello, World!'

```

## Logging

```text
INFO	ordeq.runner	Running view "hello" in module "__main__"
INFO	ordeq.io	Loading Literal('Jane')
INFO	ordeq.runner	Running view "hello_from_someone" in module "__main__"
INFO	ordeq.runner	Running view "n" in module "__main__"

```