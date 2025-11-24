## Resource

```python
from pprint import pprint

import example_project.nodes_import
from ordeq._scan import _scan_fqns

nodes, ios = _scan_fqns(example_project.nodes_import)
print("Nodes:")
pprint(sorted(nodes, key=lambda n: n.ref), width=40)
print("IOs:")
pprint(list(ios.values()), width=40)

```

## Output

```text
Nodes:
[Node(module=example_project.nodes_import, name=func_a, inputs=[Input(id=ID1), StringBuffer(_buffer=<_io.StringIO object at HASH1>)], outputs=[Print()]),
 Node(module=example_project.nodes_import, name=func_b, inputs=[Input(id=ID1), StringBuffer(_buffer=<_io.StringIO object at HASH1>)], outputs=[Print()], attributes={'tags': {'viz': 'orange'}})]
IOs:
[[FQN(module='example_project.nodes_import', name='a')],
 [FQN(module='example_project.nodes_import', name='b')],
 [FQN(module='example_project.nodes_import', name='f')]]

```