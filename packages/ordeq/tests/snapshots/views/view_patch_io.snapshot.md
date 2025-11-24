## Resource

```python
from ordeq import Input, node, run

hello_io = Input[str]("Hello")


@node(inputs=hello_io)
def hello_world(hello: str) -> tuple[str, str]:
    return hello, "World!"


@node(inputs=hello_world)
def n(v: tuple[str, ...]):
    print(f"Node received '{' '.join(v)}'")


run(n, verbose=True, io={hello_io: Input[str]("Buenos dias")})

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
DEBUG	ordeq.io	Persisting data for Input(id=ID1)
DEBUG	ordeq.io	Persisting data for Input(id=ID2)
DEBUG	ordeq.io	Loading cached data for Input(id=ID2)
DEBUG	ordeq.io	Persisting data for Input(id=ID2)
INFO	ordeq.runner	Running view 'hello_world' in module '__main__'
DEBUG	ordeq.io	Persisting data for IO(id=ID3)
DEBUG	ordeq.io	Loading cached data for IO(id=ID3)
DEBUG	ordeq.io	Persisting data for IO(id=ID3)
INFO	ordeq.runner	Running view 'n' in module '__main__'
DEBUG	ordeq.io	Persisting data for IO(id=ID4)
DEBUG	ordeq.io	Unpersisting data for IO(id=ID3)
DEBUG	ordeq.io	Unpersisting data for IO(id=ID4)

```