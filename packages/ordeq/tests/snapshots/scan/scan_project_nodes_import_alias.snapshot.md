## Resource

```python
from pprint import pprint

import example_project.nodes_import_alias
from ordeq._scan import scan

nodes, ios = scan(example_project.nodes_import_alias)
print("Nodes:")
pprint(nodes)
print("IOs:")
pprint(list(ios.values()), width=40)

```

## Output

```text
Nodes:
{<function func at HASH1>: (('example_project.nodes_import_alias',
                                   'func'),
                                  <function func at HASH1>)}
IOs:
[(('example_project.nodes_import_alias',
   'a'),
  Literal('a')),
 (('example_project.nodes_import_alias',
   'B'),
  StringBuffer(_buffer=<_io.StringIO object at HASH2>)),
 (('example_project.nodes_import_alias',
   'h'),
  Print())]

```