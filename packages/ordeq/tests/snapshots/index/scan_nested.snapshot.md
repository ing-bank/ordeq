## Resource

```python
from pprint import pprint

import example_nested
from ordeq._index import index

nodes, ios = index(example_nested)
print("Nodes:")
pprint(nodes)
print("IOs:")
pprint(list(ios.values()), width=40)

```

## Output

```text
Nodes:
{<function world at HASH1>: (('example_nested.subpackage.subsubpackage.hello',
                                    'world'),
                                   <function world at HASH1>),
 View(name=example_nested.subpackage.subsubpackage.hello:world): (('example_nested.subpackage.subsubpackage.hello',
                                                                   'world'),
                                                                  <function world at HASH1>),
 'example_nested.subpackage.subsubpackage.hello:world': (('example_nested.subpackage.subsubpackage.hello',
                                                          'world'),
                                                         <function world at HASH1>),
 ('example_nested.subpackage.subsubpackage.hello', 'world'): (('example_nested.subpackage.subsubpackage.hello',
                                                               'world'),
                                                              <function world at HASH1>)}
IOs:
[]

```