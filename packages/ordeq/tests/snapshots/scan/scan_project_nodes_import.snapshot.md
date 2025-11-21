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
[(('example_project.nodes_import', 'func_a'),
  Node(func=example_project.nodes_import:func_a, inputs=[Literal('a'), StringBuffer(_buffer=<_io.StringIO object at HASH1>)], outputs=[Print()])),
 (('example_project.nodes_import', 'func_b'),
  Node(func=example_project.nodes_import:func_b, inputs=[Literal('a'), StringBuffer(_buffer=<_io.StringIO object at HASH1>)], outputs=[Print()], attributes={'tags': {'viz': 'orange'}}))]
IOs:
[(('example_project.nodes_import', 'a'),
  Literal('a')),
 (('example_project.nodes_import', 'b'),
  StringBuffer(_buffer=<_io.StringIO object at HASH1>)),
 (('example_project.nodes_import', 'f'),
  Print())]

```