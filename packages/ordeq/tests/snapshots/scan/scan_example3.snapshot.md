## Resource

```python
from pprint import pprint

import example_3
from ordeq._resolve import _resolve_packages_to_modules
from ordeq._scan import scan

nodes, ios = scan(*_resolve_packages_to_modules(example_3))
print("Nodes:")
pprint(nodes, width=200)
print("IOs:")
pprint(list(ios.values()), width=200)

```

## Output

```text
Nodes:
{<function hello at HASH1>: ('example_3.nodes', 'f1'), <function hello at HASH2>: ('example_3.nodes', 'f2')}
IOs:
[]

```