## Resource

```python
from pprint import pprint

import example_anonymous
from ordeq._resolve import _resolve_packages_to_modules
from ordeq._scan import scan

nodes, ios = scan(*_resolve_packages_to_modules(example_anonymous))
print("Nodes:")
pprint(list(nodes.values()), width=200)
print("IOs:")
pprint(list(ios.values()), width=200)

```

## Output

```text
Nodes:
[('example_anonymous.nodes', 'node_with_inline_io')]
IOs:
[]

```