## Resource

```python
from pprint import pprint

import example_imports.assign_same_name
from ordeq._index import index

nodes, ios = index(example_imports.assign_same_name)
print("Nodes:")
pprint(nodes)
print("IOs:")
pprint(list(ios.values()), width=40)

```

## Output

```text
Nodes:
{}
IOs:
[(('example_imports.assign_same_name',
   'a'),
  IO(id=ID1)),
 (('example_imports.assign_same_name',
   'a'),
  IO(id=ID1)),
 (('example_imports.assign_same_name',
   'a'),
  IO(id=ID1))]

```