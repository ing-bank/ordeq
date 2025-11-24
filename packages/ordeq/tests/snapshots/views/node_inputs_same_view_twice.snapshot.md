## Resource

```python
from ordeq import node, run
from ordeq_common import Print


@node
def hello() -> str:
    return "Hello, World!"


print(repr(hello))


@node(inputs=[hello, hello], outputs=Print())
def n(fst: str, snd: str) -> str:
    return f"{fst} == {snd}'"


run(n, verbose=True)

```

## Output

```text
View(func=__main__:hello)
View:View(func=__main__:hello, ...) --> io-0
io-0 --> Node:__main__:n
io-0 --> Node:__main__:n
Node:__main__:n --> io-1
Hello, World! == Hello, World!'

```

## Logging

```text
INFO	ordeq.runner	Running view View(func=__main__:hello, ...)
DEBUG	ordeq.io	Persisting data for IO(id=ID1)
DEBUG	ordeq.io	Loading cached data for IO(id=ID1)
DEBUG	ordeq.io	Persisting data for IO(id=ID1)
DEBUG	ordeq.io	Loading cached data for IO(id=ID1)
DEBUG	ordeq.io	Persisting data for IO(id=ID1)
INFO	ordeq.runner	Running node 'n' in module '__main__'
INFO	ordeq.io	Saving Print()
DEBUG	ordeq.io	Unpersisting data for IO(id=ID1)

```