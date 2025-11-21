## Resource

```python
from pprint import pprint

import example_3
from ordeq._resolve import _resolve_packages_to_modules
from ordeq._scan import scan

nodes, ios = scan(*_resolve_packages_to_modules(example_3))
print("Nodes:")
pprint(nodes)
print("IOs:")
pprint(ios, width=40)

```

## Output

```text
Nodes:
[(('example_3.nodes', 'f1'), View(func=<function hello at HASH1>)),
 (('example_3.nodes', 'f2'), View(func=<function hello at HASH2>))]
IOs:
[]

```