## Resource

```python
from pprint import pp

import example_2
from ordeq._resolve import _resolve_packages_to_modules
from ordeq._scan import _scan_fqns

nodes, ios = _scan_fqns(*_resolve_packages_to_modules(example_2))
print("Nodes:")
pp(nodes, width=40)
print("IOs:")
pp(list(ios.values()), width=40)

```

## Output

```text
Nodes:
{Node(module=example_2.nodes, name=transform_input_2, inputs=[IO(id=ID1)], outputs=[Output(id=ID2)]): [FQN(module='example_2.nodes', name='transform_input_2')]}
IOs:
[[FQN(module='example_2.catalog', name='TestInput2'),
  FQN(module='example_2.nodes', name='TestInput2')],
 [FQN(module='example_2.catalog', name='TestOutput2'),
  FQN(module='example_2.nodes', name='TestOutput2')]]

```