## Resource

```python
from ordeq import node


@node(outputs=None)
def view() -> str:
    return "Hello, World!"

```

## Logging

```text
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'view_outputs_none:view'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 

```