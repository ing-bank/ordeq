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
View(name=__main__:hello)
View(name=__main__:hello_from_someone, inputs=[Literal('Jane'), View(name=__main__:hello)])
View:__main__:hello --> io-3
io-3 --> View:__main__:hello_from_someone
io-2 --> View:__main__:hello_from_someone
View:__main__:hello_from_someone --> io-0
io-0 --> View:__main__:n
View:__main__:n --> io-1
I heard that Jane said 'Hello, World!'

```

## Logging

```text
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node '__main__:hello'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node '__main__:hello_from_someone'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node '__main__:n'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
INFO	ordeq.runner	Running view "hello" in module "__main__"
INFO	ordeq.io	Loading Literal('Jane')
INFO	ordeq.runner	Running view "hello_from_someone" in module "__main__"
INFO	ordeq.runner	Running view "n" in module "__main__"

```