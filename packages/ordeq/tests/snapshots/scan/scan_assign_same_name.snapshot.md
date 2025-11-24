## Resource

```python
from pprint import pp

import example_imports.assign_same_name
from ordeq._scan import _scan_fqns

nodes, ios = _scan_fqns(example_imports.assign_same_name)
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
[[FQN(module='example_imports.assign_same_name', name='a')]]

```