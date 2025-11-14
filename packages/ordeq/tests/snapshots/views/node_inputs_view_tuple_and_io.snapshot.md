## Resource

```python
from ordeq import node, run
from ordeq._nodes import get_node
from ordeq_common import Literal, Print


@node
def hello() -> tuple[str, str]:
    return "Hello", "world"


print(repr(get_node(hello)))


@node(inputs=[hello, Literal("!!!")], outputs=Print())
def combine_greeting_with_ending(greeting: tuple[str, str], e: str):
    return f"{' '.join(greeting)} {e}"


run(combine_greeting_with_ending, verbose=True)

```

## Output

```text
View(name=__main__:hello)
View:__main__:hello --> io-1
io-0 --> Node:__main__:combine_greeting_with_ending
io-1 --> Node:__main__:combine_greeting_with_ending
Node:__main__:combine_greeting_with_ending --> io-2
Hello world !!!

```

## Logging

```text
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node '__main__:hello'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
INFO	ordeq.runner	Running view "hello" in module "__main__"
INFO	ordeq.io	Loading Literal('!!!')
INFO	ordeq.runner	Running node "combine_greeting_with_ending" in module "__main__"
INFO	ordeq.io	Saving Print()

```