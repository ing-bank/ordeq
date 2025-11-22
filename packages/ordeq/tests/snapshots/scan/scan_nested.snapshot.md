## Resource

```python
from pprint import pprint

import example_nested
from ordeq._resolve import _resolve_packages_to_modules
from ordeq._scan import scan

nodes, ios = scan(*_resolve_packages_to_modules(example_nested))
print("Nodes:")
pprint(list(nodes.values()), width=200)
print("IOs:")
pprint(list(ios.values()), width=200)

```

## Output

```text
Nodes:
[('example_nested.subpackage.subsubpackage.hello', 'world')]
IOs:
[]

```