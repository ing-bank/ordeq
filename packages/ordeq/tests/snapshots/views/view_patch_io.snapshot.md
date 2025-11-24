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
io-0 --> View:__main__:hello_world
View:__main__:hello_world --> io-1
io-1 --> View:__main__:n
View:__main__:n --> io-2
Node received 'Buenos dias World!'

```

## Logging

```text
INFO	ordeq.io	Loading Literal('Buenos dias')
INFO	ordeq.runner	Running view '__main__:hello_world'
INFO	ordeq.runner	Running view '__main__:n'

```