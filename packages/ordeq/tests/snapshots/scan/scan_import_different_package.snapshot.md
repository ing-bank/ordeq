## Resource

```python
from pprint import pprint

import example_imports.import_different_package
from ordeq._scan import scan

nodes, ios = scan(example_imports.import_different_package)
print("Nodes:")
pprint(nodes)
print("IOs:")
pprint(ios, width=40)

```

## Output

```text
Nodes:
[]
IOs:
[(('example_imports.import_different_package',
   'Hello'),
  StringBuffer(_buffer=<_io.StringIO object at HASH1>))]

```