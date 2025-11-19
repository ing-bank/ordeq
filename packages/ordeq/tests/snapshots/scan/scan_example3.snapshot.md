## Resource

```python
from pprint import pprint

import example_3
from ordeq._scan import scan

nodes, ios = scan(example_3)
print("Nodes:")
pprint(nodes)
print("IOs:")
pprint(ios, width=40)

```

## Output

```text
Nodes:
[(('example_3.nodes', 'f1'), View(name=example_3.func_defs:hello)),
 (('example_3.nodes', 'f2'), View(name=example_3.func_defs:hello))]
IOs:
[]

```