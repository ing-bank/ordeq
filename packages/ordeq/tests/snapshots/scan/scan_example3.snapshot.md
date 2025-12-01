## Resource

```python
from pprint import pp

import example_3
from ordeq._resolve import _resolve_packages_to_modules
from ordeq._scan import _scan_fqns

nodes, ios = _scan_fqns(*_resolve_packages_to_modules(example_3))
print("Nodes:")
pp(nodes, width=40)
print("IOs:")
pp(list(ios.values()), width=40)

```

## Output

```text
Nodes:
{View(func=example_3.func_defs:hello): [FQN(module='example_3.nodes', name='f1')],
 View(func=example_3.func_defs:hello): [FQN(module='example_3.nodes', name='f2')]}
IOs:
[]

```