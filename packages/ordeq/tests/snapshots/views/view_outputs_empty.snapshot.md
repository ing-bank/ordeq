## Resource

```python
from ordeq import node


@node(outputs=[])
def view() -> str:
    return "Hello, World!"

```

## Logging

```text
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'view_outputs_empty:view'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 

```