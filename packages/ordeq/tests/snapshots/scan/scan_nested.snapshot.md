## Resource

```python
from pprint import pprint

import example_nested
from ordeq._resolve import _resolve_packages_to_modules
from ordeq._scan import scan

nodes, ios = scan(*_resolve_packages_to_modules(example_nested))
print("Nodes:")
pprint(nodes)
print("IOs:")
pprint(ios, width=40)

```

## Output

```text
Nodes:
[(FQN(module='example_nested.subpackage.subsubpackage.hello', name='world'),
  View(func=example_nested.subpackage.subsubpackage.hello:world))]
IOs:
[]

```