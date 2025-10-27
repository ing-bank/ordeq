## Resource

```python
from ordeq import node
from ordeq_common import StringBuffer

node_1 = node(inputs=(), outputs=(), func=lambda: None)
node_2 = node(inputs=(), outputs=(StringBuffer(),), func=lambda: "bluh")

pipeline = {node_1, node_2}

# TODO: run these!

```

## Logging

```text
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'node_without_decorators:<lambda>'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 

```