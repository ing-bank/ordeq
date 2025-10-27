## Resource

```python
from ordeq import node


@node
def func(x: str) -> str:
    return x

```

## Exception

```text
ValueError: Node inputs invalid for function arguments: Node(name=node_late_binding:func,...)
```

## Logging

```text
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'node_late_binding:func'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 

```