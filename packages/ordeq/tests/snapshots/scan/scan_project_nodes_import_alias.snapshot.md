## Resource

```python
from pprint import pprint

import example_project.nodes_import_alias
from ordeq._scan import _scan_fqns

nodes, ios = _scan_fqns(example_project.nodes_import_alias)
print("Nodes:")
pprint(sorted(nodes, key=lambda n: (nodes[n], n.ref)), width=40)
print("IOs:")
pprint(list(ios.values()), width=40)

```

## Output

```text
Nodes:
[Node(module=example_project.nodes_import_alias, name=func, inputs=[Input(id=ID1), StringBuffer(_buffer=<_io.StringIO object at HASH1>)], outputs=[Print()], attributes={'tags': {'key': 'threshold', 'value': 0.23}})]
IOs:
[[FQN(module='example_project.nodes_import_alias', name='a')],
 [FQN(module='example_project.nodes_import_alias', name='B')],
 [FQN(module='example_project.nodes_import_alias', name='h')]]

```