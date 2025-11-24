## Resource

```python
from pprint import pprint

import example_anonymous
from ordeq._scan import _scan_fqns

nodes, ios = _scan_fqns(example_anonymous)
print("Nodes:")
pprint(nodes)
print("IOs:")
pprint(list(ios.values()), width=40)

```

## Output

```text
Nodes:
{Node(module=example_anonymous.nodes, name=node_with_inline_io, inputs=[IO(id=ID1)], outputs=[IO(id=ID2)]): [FQN(module='example_anonymous.nodes', name='node_with_inline_io')]}
IOs:
[]

```