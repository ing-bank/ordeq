## Resource

```python
from pprint import pp

import example_imports.aliased_catalog
from ordeq._scan import _scan_fqns
from ordeq._resolve import _resolve_packages_to_modules

nodes, ios = _scan_fqns(*_resolve_packages_to_modules(example_imports.aliased_catalog))
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
[[FQN(module='example_imports.aliased_catalog', name='a')]]

```