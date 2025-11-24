## Resource

```python
from pprint import pprint

import example_project.nodes_import_alias
from ordeq._scan import scan

nodes, ios = scan(example_project.nodes_import_alias)
print("Nodes:")
pprint(nodes)
print("IOs:")
pprint(ios, width=40)

```

## Output

```text
Nodes:
[(FQN(module='example_project.nodes_import_alias', name='func'),
  Node(module=example_project.nodes_import_alias, name=func, inputs=[Literal('a'), StringBuffer(_buffer=<_io.StringIO object at HASH1>)], outputs=[Print()], attributes={'tags': {'key': 'threshold', 'value': 0.23}}))]
IOs:
[(FQN(module='example_project.nodes_import_alias', name='a'),
  Literal('a')),
 (FQN(module='example_project.nodes_import_alias', name='B'),
  StringBuffer(_buffer=<_io.StringIO object at HASH1>)),
 (FQN(module='example_project.nodes_import_alias', name='h'),
  Print())]

```