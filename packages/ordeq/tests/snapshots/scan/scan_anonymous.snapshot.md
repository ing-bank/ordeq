## Resource

```python
from pprint import pprint

import example_anonymous
from ordeq._resolve import _resolve_packages_to_modules
from ordeq._scan import scan

nodes, ios = scan(*_resolve_packages_to_modules(example_anonymous))
print("Nodes:")
pprint(nodes)
print("IOs:")
pprint(ios, width=40)

```

## Output

```text
Nodes:
[(('example_anonymous.nodes', 'node_with_inline_io'),
  Node(func=example_anonymous.nodes:node_with_inline_io, inputs=[IO(id=ID1)], outputs=[IO(id=ID2)]))]
IOs:
[]

```