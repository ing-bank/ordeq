## Resource

```python
from pprint import pprint

import example_3
from ordeq._scan import _scan_fqns

nodes, ios = _scan_fqns(example_3)
print("Nodes:")
pprint(sorted(nodes, key=lambda n: n.ref), width=40)
print("IOs:")
pprint(list(ios.values()), width=40)

```

## Output

```text
Nodes:
[View(func=example_3.func_defs:hello),
 View(func=example_3.func_defs:hello)]
IOs:
[]

```