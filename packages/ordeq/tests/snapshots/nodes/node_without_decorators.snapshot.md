## Resource

```python
from ordeq import node
from ordeq_common import StringBuffer

node_1 = node(inputs=(), outputs=(), func=lambda: None)
node_2 = node(inputs=(), outputs=(StringBuffer(),), func=lambda: "bluh")

pipeline = {node_1, node_2}

# TODO: run these!

```