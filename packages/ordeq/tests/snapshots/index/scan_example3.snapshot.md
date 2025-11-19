## Resource

```python
from pprint import pprint

import example_3
from ordeq._index import index

nodes, ios = index(example_3)
print("Nodes:")
pprint(nodes)
print("IOs:")
pprint(ios, width=40)

```

## Output

```text
Nodes:
{<function hello at HASH1>: (('example_3.nodes', 'f1'),
                                   <function hello at HASH1>),
 <function hello at HASH2>: (('example_3.nodes', 'f2'),
                                   <function hello at HASH2>),
 View(name=example_3.func_defs:hello): (('example_3.nodes', 'f1'),
                                        <function hello at HASH1>),
 View(name=example_3.func_defs:hello): (('example_3.nodes', 'f2'),
                                        <function hello at HASH2>),
 'example_3.nodes:f1': (('example_3.nodes', 'f1'),
                        <function hello at HASH1>),
 'example_3.nodes:f2': (('example_3.nodes', 'f2'),
                        <function hello at HASH2>),
 ('example_3.nodes', 'f1'): (('example_3.nodes', 'f1'),
                             <function hello at HASH1>),
 ('example_3.nodes', 'f2'): (('example_3.nodes', 'f2'),
                             <function hello at HASH2>)}
IOs:
{}

```