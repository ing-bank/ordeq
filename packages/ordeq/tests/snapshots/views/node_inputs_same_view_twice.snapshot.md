## Resource

```python
from ordeq import node, run
from ordeq._nodes import get_node
from ordeq_common import Print


@node
def hello() -> str:
    return "Hello, World!"


print(repr(get_node(hello)))


@node(inputs=[hello, hello], outputs=Print())
def n(fst: str, snd: str) -> str:
    return f"{fst} == {snd}'"


run(n, verbose=True)

```

## Output

```text
View(name=__main__:hello)
NodeResourceGraph(nodes=2, resources=2, edges={View(name=__main__:hello): [Resource(value=IO(id=ID1))], Node(name=__main__:n, inputs=[IO(id=ID1), IO(id=ID1)], outputs=[Print()]): [Resource(value=Print())], Resource(value=IO(id=ID1)): [Node(name=__main__:n, inputs=[IO(id=ID1), IO(id=ID1)], outputs=[Print()]), Node(name=__main__:n, inputs=[IO(id=ID1), IO(id=ID1)], outputs=[Print()])], Resource(value=Print()): []})
Hello, World! == Hello, World!'

```

## Logging

```text
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node '__main__:hello'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
INFO	ordeq.runner	Running view "hello" in module "__main__"
INFO	ordeq.runner	Running node "n" in module "__main__"
INFO	ordeq.io	Saving Print()

```