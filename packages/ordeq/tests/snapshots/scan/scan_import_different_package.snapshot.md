## Resource

```python
from pprint import pprint

import example_imports.import_different_package
from ordeq._scan import _scan_fqns

nodes, ios = _scan_fqns(example_imports.import_different_package)
print("Nodes:")
pprint([node for node in sorted(nodes, key=lambda n: (nodes[n], n.ref))], width=40)
print("IOs:")
pprint(list(ios.values()), width=40)

```

## Output

```text
Nodes:
[]
IOs:
[[FQN(module='example_imports.import_different_package', name='Hello')]]

```