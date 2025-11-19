## Resource

```python
from ordeq import node, run
from ordeq_common import Print

glob = 2


@node
def conditional() -> str | None:
    if glob > 2:
        return "Higher value!"
    return None


@node(inputs=conditional, outputs=Print())
def n(v: str | None):
    return v


glob = 3
run(n, verbose=True)

glob = 1
run(n, verbose=True)

```

## Output

```text
NodeResourceGraph(edges={View(name=__main__:conditional): [Resource(value=IO(id=ID1))], Node(name=__main__:n, inputs=[IO(id=ID1)], outputs=[Print()]): [Resource(value=Print())], Resource(value=IO(id=ID1)): [Node(name=__main__:n, inputs=[IO(id=ID1)], outputs=[Print()])], Resource(value=Print()): []})
Higher value!
NodeResourceGraph(edges={View(name=__main__:conditional): [Resource(value=IO(id=ID1))], Node(name=__main__:n, inputs=[IO(id=ID1)], outputs=[Print()]): [Resource(value=Print())], Resource(value=IO(id=ID1)): [Node(name=__main__:n, inputs=[IO(id=ID1)], outputs=[Print()])], Resource(value=Print()): []})
None

```

## Logging

```text
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node '__main__:conditional'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
INFO	ordeq.runner	Running view "conditional" in module "__main__"
INFO	ordeq.runner	Running node "n" in module "__main__"
INFO	ordeq.io	Saving Print()
INFO	ordeq.runner	Running view "conditional" in module "__main__"
INFO	ordeq.runner	Running node "n" in module "__main__"
INFO	ordeq.io	Saving Print()

```