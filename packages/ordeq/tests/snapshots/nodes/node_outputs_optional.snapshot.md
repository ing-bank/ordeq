## Resource

```python
from ordeq import node
from ordeq_common import StringBuffer


@node(inputs=[StringBuffer("a")])
def func(x: str) -> None:
    print(x)

```

## Logging

```text
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'node_outputs_optional:func'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 

```