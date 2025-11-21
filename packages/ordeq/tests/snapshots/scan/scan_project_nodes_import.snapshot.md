## Resource

```python
from pprint import pprint

import example_project.nodes_import
from ordeq._scan import scan

nodes, ios = scan(example_project.nodes_import)
print("Nodes:")
pprint(nodes)
print("IOs:")
pprint(list(ios.values()), width=40)

```

## Output

```text
Nodes:
{<function func_a at HASH1>: (('example_project.nodes_import', 'func_a'),
                                    <function func_a at HASH1>),
 <function func_b at HASH2>: (('example_project.nodes_import', 'func_b'),
                                    <function func_b at HASH2>)}
IOs:
[(('example_project.nodes_import', 'a'),
  Literal('a')),
 (('example_project.nodes_import', 'b'),
  StringBuffer(_buffer=<_io.StringIO object at HASH3>)),
 (('example_project.nodes_import', 'f'),
  Print())]

```