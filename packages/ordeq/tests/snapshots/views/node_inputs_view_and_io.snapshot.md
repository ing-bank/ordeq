## Resource

```python
from ordeq import node, run
from ordeq._nodes import get_node
from ordeq_common import Literal, Print


@node
def hello() -> str:
    return "Hello, World!"


print(repr(get_node(hello)))


@node(inputs=[Literal("Jane"), hello], outputs=Print())
def n(name: str, greeting: str) -> str:
    return f"{name} said '{greeting}'"


run(n, verbose=True)

```

## Output

```text
View(name=__main__:hello)
NodeResourceGraph(nodes=2, resources=3, edges={View(name=__main__:hello): [Resource(value=IO(id=ID1))], Node(name=__main__:n, inputs=[Literal('Jane'), IO(id=ID1)], outputs=[Print()]): [Resource(value=Print())], Resource(value=IO(id=ID1)): [Node(name=__main__:n, inputs=[Literal('Jane'), IO(id=ID1)], outputs=[Print()])], Resource(value=Literal('Jane')): [Node(name=__main__:n, inputs=[Literal('Jane'), IO(id=ID1)], outputs=[Print()])], Resource(value=Print()): []})
Jane said 'Hello, World!'

```

## Logging

```text
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node '__main__:hello'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
INFO	ordeq.runner	Running view "hello" in module "__main__"
INFO	ordeq.io	Loading Literal('Jane')
INFO	ordeq.runner	Running node "n" in module "__main__"
INFO	ordeq.io	Saving Print()

```