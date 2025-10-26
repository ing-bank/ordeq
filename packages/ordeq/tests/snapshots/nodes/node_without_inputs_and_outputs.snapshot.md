## Resource

```python
from ordeq import node


@node()
def func() -> None:
    pass

```

## Logging

```text
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'node_without_inputs_and_outputs:func'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 

```