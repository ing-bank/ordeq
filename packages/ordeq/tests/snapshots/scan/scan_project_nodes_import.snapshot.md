## Resource

```python
from pprint import pp

import example_project.nodes_import
from ordeq._resolve import _resolve_packages_to_modules
from ordeq._scan import _scan_fqns

nodes, ios = _scan_fqns(
    *_resolve_packages_to_modules(example_project.nodes_import)
)
print("Nodes:")
pp(nodes, width=40)
print("IOs:")
pp(list(ios.values()), width=40)

```

## Output

```text
Nodes:
{Node(module=example_project.nodes_import, name=func_a, inputs=[IO(id=ID1), IO(id=ID2)], outputs=[Print()]): [FQN(module='example_project.nodes_import', name='func_a')],
 Node(module=example_project.nodes_import, name=func_b, inputs=[IO(id=ID1), IO(id=ID2)], outputs=[Print()], attributes={'tags': {'viz': 'orange'}}): [FQN(module='example_project.nodes_import', name='func_b')]}
IOs:
[[FQN(module='example_project.nodes_import', name='a')],
 [FQN(module='example_project.nodes_import', name='b')],
 [FQN(module='example_project.nodes_import', name='f')]]

```