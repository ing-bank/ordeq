## Resource

```python
from ordeq import Input, node, run
from ordeq_common import Print


@node
def hello() -> tuple[str, str]:
    return "Hello", "world"


print(repr(hello))


@node(inputs=[hello, Input[str]("!!!")], outputs=Print())
def combine_greeting_with_ending(greeting: tuple[str, str], e: str):
    return f"{' '.join(greeting)} {e}"


run(combine_greeting_with_ending, verbose=True)

```

## Output

```text
View(func=__main__:hello)
View:View(func=__main__:hello, ...) --> io-1
io-0 --> Node:__main__:combine_greeting_with_ending
io-1 --> Node:__main__:combine_greeting_with_ending
Node:__main__:combine_greeting_with_ending --> io-2
Hello world !!!

```

## Logging

```text
DEBUG	ordeq.io	Persisting data for Input(id=ID1)
INFO	ordeq.runner	Running view View(func=__main__:hello, ...)
DEBUG	ordeq.io	Persisting data for IO(id=ID2)
DEBUG	ordeq.io	Loading cached data for IO(id=ID2)
DEBUG	ordeq.io	Persisting data for IO(id=ID2)
DEBUG	ordeq.io	Loading cached data for Input(id=ID1)
DEBUG	ordeq.io	Persisting data for Input(id=ID1)
INFO	ordeq.runner	Running node 'combine_greeting_with_ending' in module '__main__'
INFO	ordeq.io	Saving Print()
DEBUG	ordeq.io	Unpersisting data for IO(id=ID2)

```