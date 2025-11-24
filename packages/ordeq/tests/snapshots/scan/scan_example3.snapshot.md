## Resource

```python
from pprint import pprint

import example_3
from ordeq._scan import _scan_fqns

nodes, ios = _scan_fqns(example_3)
print("Nodes:")
pprint(nodes, width=40)
print("IOs:")
pprint(list(ios.values()), width=40)

```

## Output

```text
Nodes:
{View(func=example_3.func_defs:hello): [FQN(module='example_3.nodes', name='f1')],
 View(func=example_3.func_defs:hello): [FQN(module='example_3.nodes', name='f2')]}
IOs:
[]

```