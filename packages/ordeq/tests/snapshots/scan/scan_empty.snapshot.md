## Resource

```python
from pprint import pprint

import example_empty
from ordeq._scan import _scan_fqns

nodes, ios = _scan_fqns(example_empty)
print("Nodes:")
pprint(sorted(nodes, key=lambda n: (nodes[n], n.ref)), width=40)
print("IOs:")
pprint(list(ios.values()), width=40)

```

## Output

```text
Nodes:
[]
IOs:
[]

```