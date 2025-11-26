## Resource

```python
from pprint import pp

import example_imports.import_different_package
from ordeq._resolve import _resolve_packages_to_modules
from ordeq._scan import _scan_fqns

nodes, ios = _scan_fqns(
    *_resolve_packages_to_modules(example_imports.import_different_package)
)
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
[[FQN(module='example_imports.import_different_package', name='Hello')]]

```