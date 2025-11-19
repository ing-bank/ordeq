## Resource

```python
from pprint import pprint

import example_project.nodes_import_alias
from ordeq._scan import scan

nodes, ios = scan(example_project.nodes_import_alias)
print("Nodes:")
pprint(nodes)
print("IOs:")
pprint(ios)

```

## Output

```text
Nodes:
[(('example_project.nodes_import_alias', 'func'),
  Node(name=example_project.nodes_import_alias:func, inputs=[Literal('a'), StringBuffer(_buffer=<_io.StringIO object at HASH1>)], outputs=[Print()], attributes={'tags': {'key': 'threshold', 'value': 0.23}}))]
IOs:
[(('example_project.nodes_import_alias', 'a'), Literal('a')),
 (('example_project.nodes_import_alias', 'B'),
  StringBuffer(_buffer=<_io.StringIO object at HASH1>)),
 (('example_project.nodes_import_alias', 'h'), Print())]

```