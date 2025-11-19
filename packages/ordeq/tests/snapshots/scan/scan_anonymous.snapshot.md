## Resource

```python
from pprint import pprint

import example_anonymous
from ordeq._scan import scan

nodes, ios = scan(example_anonymous)
print("Nodes:")
pprint(nodes)
print("IOs:")
pprint(ios)

```

## Output

```text
Nodes:
[(('example_anonymous.nodes', 'node_with_inline_io'),
  Node(name=example_anonymous.nodes:node_with_inline_io, inputs=[IO(id=ID1)], outputs=[IO(id=ID2)]))]
IOs:
[]

```