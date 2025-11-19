## Resource

```python
from pprint import pprint

import example_project.nodes_import
from ordeq._scan import scan

nodes, ios = scan(example_project.nodes_import)
print("Nodes:")
pprint(list(nodes.items()))
print("IOs:")
pprint(list(ios.values()))

```

## Output

```text
Nodes:
[(Node(name=example_project.nodes_import:func_a, inputs=[Literal('a'), StringBuffer(_buffer=<_io.StringIO object at HASH1>)], outputs=[Print()]),
  [('example_project.nodes_import', 'func_a')]),
 (Node(name=example_project.nodes_import:func_b, inputs=[Literal('a'), StringBuffer(_buffer=<_io.StringIO object at HASH1>)], outputs=[Print()], attributes={'tags': {'viz': 'orange'}}),
  [('example_project.nodes_import', 'func_b')])]
IOs:
[[(('example_project.nodes_import', 'a'), Literal('a'))],
 [(('example_project.nodes_import', 'b'),
   StringBuffer(_buffer=<_io.StringIO object at HASH1>))],
 [(('example_project.nodes_import', 'f'), Print())]]

```