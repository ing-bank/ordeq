## Resource

```python
from pprint import pprint

import example_project
from ordeq._scan import scan

nodes, ios = scan(example_project)
print("Nodes:")
pprint(nodes)
print("IOs:")
pprint(ios)

```

## Output

```text
Nodes:
[(('example_project.inner.nodes', 'func'),
  Node(name=example_project.inner.nodes:func, inputs=[IO(id=ID1)], outputs=[Print()], attributes={'tags': ['dummy']})),
 (('example_project.nodes', 'func'),
  Node(name=example_project.nodes:func, inputs=[IO(id=ID2)], outputs=[Print()], attributes={'tags': ['dummy']})),
 (('example_project.nodes_import', 'func_a'),
  Node(name=example_project.nodes_import:func_a, inputs=[Literal('a'), StringBuffer(_buffer=<_io.StringIO object at HASH1>)], outputs=[Print()])),
 (('example_project.nodes_import', 'func_b'),
  Node(name=example_project.nodes_import:func_b, inputs=[Literal('a'), StringBuffer(_buffer=<_io.StringIO object at HASH1>)], outputs=[Print()], attributes={'tags': {'viz': 'orange'}})),
 (('example_project.nodes_import_alias', 'func'),
  Node(name=example_project.nodes_import_alias:func, inputs=[Literal('a'), StringBuffer(_buffer=<_io.StringIO object at HASH1>)], outputs=[Print()], attributes={'tags': {'key': 'threshold', 'value': 0.23}})),
 (('example_project.nodes_with_inline_io', 'greet'),
  Node(name=example_project.nodes_with_inline_io:greet, inputs=[Literal('Buenos dias')], outputs=[IO(id=ID3)])),
 (('example_project.nodes_with_view', 'greet'),
  View(name=example_project.nodes_with_view:greet, inputs=[Literal('Hello')])),
 (('example_project.nodes_with_view', 'farewell'),
  Node(name=example_project.nodes_with_view:farewell, inputs=[IO(id=ID4)], outputs=[Print()]))]
IOs:
[(('example_project.catalog_1', 'a'), Literal('a')),
 (('example_project.catalog_1', 'b'),
  StringBuffer(_buffer=<_io.StringIO object at HASH1>)),
 (('example_project.catalog_1', 'c'), Print()),
 (('example_project.catalog_2', 'd'), Literal('a')),
 (('example_project.catalog_2', 'e'),
  StringBuffer(_buffer=<_io.StringIO object at HASH2>)),
 (('example_project.catalog_2', 'f'), Print()),
 (('example_project.catalog_2', 'g'), Print()),
 (('example_project.catalog_2', 'h'), Print()),
 (('example_project.catalog_2', 'i'), Print()),
 (('example_project.catalog_2', 'j'), Print()),
 (('example_project.inner.nodes', 'x'), IO(id=ID1)),
 (('example_project.inner.nodes', 'y'), Print()),
 (('example_project.nodes', 'x'), IO(id=ID2)),
 (('example_project.nodes', 'y'), Print()),
 (('example_project.nodes_import', 'a'), Literal('a')),
 (('example_project.nodes_import', 'b'),
  StringBuffer(_buffer=<_io.StringIO object at HASH1>)),
 (('example_project.nodes_import', 'f'), Print()),
 (('example_project.nodes_import_alias', 'a'), Literal('a')),
 (('example_project.nodes_import_alias', 'B'),
  StringBuffer(_buffer=<_io.StringIO object at HASH1>)),
 (('example_project.nodes_import_alias', 'h'), Print()),
 (('example_project.nodes_with_view', 'greeting'), Literal('Hello')),
 (('example_project.nodes_with_view', 'printer'), Print())]

```