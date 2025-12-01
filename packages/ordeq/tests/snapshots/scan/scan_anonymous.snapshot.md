## Resource

```python
from pprint import pp

import example_anonymous
from ordeq._resolve import _resolve_packages_to_modules
from ordeq._scan import _scan_fqns

nodes, ios = _scan_fqns(*_resolve_packages_to_modules(example_anonymous))
print("Nodes:")
pp(nodes, width=40)
print("IOs:")
pp(list(ios.values()), width=40)

```

## Output

```text
Nodes:
{View(module=example_anonymous.node_with_var_names, name=add, inputs=[Input(id=ID1), Input(id=ID2)]): [FQN(module='example_anonymous.node_with_var_names', name='add')],
 Node(module=example_anonymous.nodes, name=node_with_inline_io, inputs=[IO(id=ID3)], outputs=[IO(id=ID4)]): [FQN(module='example_anonymous.nodes', name='node_with_inline_io')]}
IOs:
[]

```