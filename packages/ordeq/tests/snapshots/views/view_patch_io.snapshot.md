## Resource

```python
from ordeq import node, run
from ordeq_common import Literal

hello_io = Literal("Hello")


@node(inputs=hello_io)
def hello_world(hello: str) -> tuple[str, str]:
    return hello, "World!"


@node(inputs=hello_world)
def n(v: tuple[str, ...]):
    print(f"Node received '{' '.join(v)}'")


run(n, verbose=True, io={hello_io: Literal("Buenos dias")})

```

## Output

```text
io-2 --> View:__main__:hello_world
View:__main__:hello_world --> io-0
io-0 --> View:__main__:n
View:__main__:n --> io-1
Node received 'Buenos dias World!'

```

## Logging

```text
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node '__main__:hello_world'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node '__main__:n'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
INFO	ordeq.io	Loading Literal('Buenos dias')
INFO	ordeq.runner	Running view "hello_world" in module "__main__"
INFO	ordeq.runner	Running view "n" in module "__main__"

```