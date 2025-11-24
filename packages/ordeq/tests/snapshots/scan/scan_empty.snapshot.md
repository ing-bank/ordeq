## Resource

```python
from pprint import pp

import example_empty
from ordeq._scan import _scan_fqns

nodes, ios = _scan_fqns(example_empty)
print("Nodes:")
pp(nodes, width=40)
print("IOs:")
pp(list(ios.values()), width=40)

```

## Output

```text
Nodes:
{}
IOs:
[]

```