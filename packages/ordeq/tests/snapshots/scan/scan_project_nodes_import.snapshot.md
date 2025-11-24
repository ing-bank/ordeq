## Resource

```python
from pprint import pprint

import example_project.nodes_import
from ordeq._scan import scan

nodes, ios = scan(example_project.nodes_import)
print("Nodes:")
pprint(nodes)
print("IOs:")
pprint(ios, width=40)

```

## Output

```text
Nodes:
[(FQN(module='example_project.nodes_import', name='func_a'),
  Node(module=example_project.nodes_import, name=func_a, inputs=[Input(id=ID1), StringBuffer(_buffer=<_io.StringIO object at HASH1>)], outputs=[Print()])),
 (FQN(module='example_project.nodes_import', name='func_b'),
  Node(module=example_project.nodes_import, name=func_b, inputs=[Input(id=ID1), StringBuffer(_buffer=<_io.StringIO object at HASH1>)], outputs=[Print()], attributes={'tags': {'viz': 'orange'}}))]
IOs:
[(FQN(module='example_project.nodes_import', name='a'),
  Input(id=ID1)),
 (FQN(module='example_project.nodes_import', name='b'),
  StringBuffer(_buffer=<_io.StringIO object at HASH1>)),
 (FQN(module='example_project.nodes_import', name='f'),
  Print())]

```