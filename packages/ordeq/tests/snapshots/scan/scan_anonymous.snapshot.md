## Resource

```python
from pprint import pprint

import example_anonymous
from ordeq._scan import scan

nodes, ios = scan(example_anonymous)
print("Nodes:")
pprint(list(nodes.items()))
print("IOs:")
pprint(list(ios.values()))

```

## Output

```text
Nodes:
[(Node(name=example_anonymous.nodes:node_with_inline_io, inputs=[IO(id=ID1)], outputs=[IO(id=ID2)]),
  [('example_anonymous.nodes', 'node_with_inline_io')])]
IOs:
[]

```