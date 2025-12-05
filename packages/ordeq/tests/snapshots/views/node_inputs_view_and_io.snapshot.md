## Resource

```python
from ordeq import Input, node, run
from ordeq_common import Print


@node
def hello() -> str:
    return "Hello, World!"


print(repr(hello))


@node(inputs=[Input[str]("Jane"), hello], outputs=Print())
def n(name: str, greeting: str) -> str:
    return f"{name} said '{greeting}'"


run(n, verbose=True)

```

## Output

```text
View(func=__main__:hello)
View:View(func=__main__:hello, ...) --> io-0
io-0 --> Node:__main__:n
io-1 --> Node:__main__:n
Node:__main__:n --> io-2
Jane said 'Hello, World!'

```

## Logging

```text
DEBUG	ordeq.io	Persisting data for Input(id=ID1)
INFO	ordeq.runner	Running View(func=__main__:hello, ...)
DEBUG	ordeq.io	Persisting data for IO 'n:greeting' in module '__main__'
DEBUG	ordeq.io	Loading cached data for Input 'n:name' in module '__main__'
DEBUG	ordeq.io	Loading cached data for IO 'n:greeting' in module '__main__'
INFO	ordeq.runner	Running node 'n' in module '__main__'
INFO	ordeq.io	Saving Print()
DEBUG	ordeq.io	Unpersisting data for IO 'n:greeting' in module '__main__'

```