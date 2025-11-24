## Resource

```python
from pprint import pprint

import example_imports.local_import
from ordeq._scan import _scan_fqns

nodes, ios = _scan_fqns(example_imports.local_import)
print("Nodes:")
pprint(nodes)
print("IOs:")
pprint(list(ios.values()), width=40)

```

## Output

```text
Nodes:
{}
IOs:
[[FQN(module='example_imports.local_import', name='a')]]

```