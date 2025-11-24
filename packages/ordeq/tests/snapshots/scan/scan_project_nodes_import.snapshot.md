## Resource

```python
from pprint import pp

import example_project.nodes_import
from ordeq._scan import _scan_fqns

nodes, ios = _scan_fqns(example_project.nodes_import)
print("Nodes:")
pp(nodes, width=40)
print("IOs:")
pp(list(ios.values()), width=40)

```

## Output

```text
Nodes:
{Node(module=example_project.nodes_import, name=func_a, inputs=[Input(id=ID1), StringBuffer(_buffer=<_io.StringIO object at HASH1>)], outputs=[Print()]): [FQN(module='example_project.nodes_import', name='func_a')],
 Node(module=example_project.nodes_import, name=func_b, inputs=[Input(id=ID1), StringBuffer(_buffer=<_io.StringIO object at HASH1>)], outputs=[Print()], attributes={'tags': {'viz': 'orange'}}): [FQN(module='example_project.nodes_import', name='func_b')]}
IOs:
[[FQN(module='example_project.nodes_import', name='a')],
 [FQN(module='example_project.nodes_import', name='b')],
 [FQN(module='example_project.nodes_import', name='f')]]

```