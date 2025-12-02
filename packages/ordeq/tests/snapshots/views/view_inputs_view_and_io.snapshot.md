## Resource

```python
from ordeq import Input, node, run


@node
def hello() -> str:
    return "Hello, World!"


print(repr(hello))


@node(inputs=[Input[str]("Jane"), hello])
def hello_from_someone(name: str, v: str) -> str:
    return f"{name} said '{v}'"


print(repr(hello_from_someone))


@node(inputs=hello_from_someone)
def n(v: str) -> None:
    print(f"I heard that {v}")


run(n, verbose=True)

```

## Output

```text
View(func=__main__:hello)
View(module=__main__, name=hello_from_someone, inputs=[IO(id=ID1), IO(id=ID2)])
View:View(func=__main__:hello, ...) --> io-0
io-0 --> View:__main__:hello_from_someone
io-1 --> View:__main__:hello_from_someone
View:__main__:hello_from_someone --> io-2
io-2 --> View:__main__:n
View:__main__:n --> io-3
I heard that Jane said 'Hello, World!'

```

## Logging

```text
DEBUG	ordeq.io	Persisting data for Input(id=ID3)
DEBUG	ordeq.runner	Running Input(id=ID3)
DEBUG	ordeq.io	Loading cached data for Input(id=ID3)
DEBUG	ordeq.io	Persisting data for IO 'hello_from_someone:name' in module '__main__'
DEBUG	ordeq.runner	Running View(func=__main__:hello, ...)
DEBUG	ordeq.io	Persisting data for IO 'hello_from_someone:v' in module '__main__'
DEBUG	ordeq.io	Loading cached data for IO 'hello_from_someone:name' in module '__main__'
DEBUG	ordeq.io	Loading cached data for IO 'hello_from_someone:v' in module '__main__'
DEBUG	ordeq.runner	Running view 'hello_from_someone' in module '__main__'
DEBUG	ordeq.io	Persisting data for IO 'n:v' in module '__main__'
DEBUG	ordeq.io	Loading cached data for IO 'n:v' in module '__main__'
DEBUG	ordeq.runner	Running view 'n' in module '__main__'
DEBUG	ordeq.io	Persisting data for IO(id=ID4)
DEBUG	ordeq.io	Unpersisting data for IO 'hello_from_someone:v' in module '__main__'
DEBUG	ordeq.io	Unpersisting data for IO 'hello_from_someone:name' in module '__main__'
DEBUG	ordeq.io	Unpersisting data for IO 'n:v' in module '__main__'
DEBUG	ordeq.io	Unpersisting data for IO(id=ID4)

```