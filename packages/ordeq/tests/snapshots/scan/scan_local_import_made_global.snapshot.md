## Resource

```python
from pprint import pprint

import example_imports.local_import_made_global
from ordeq._scan import scan

nodes, ios = scan(example_imports.local_import_made_global)
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
[(('example_imports.local_import_made_global',
   'a'),
  IO(id=ID1))]

```