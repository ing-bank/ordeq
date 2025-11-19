## Resource

```python
from ordeq import node


@node
def func() -> None:
    pass

```

## Logging

```text
WARNING	ordeq.preview	Creating a view, as no outputs were provided for node '__main__:func'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 

```