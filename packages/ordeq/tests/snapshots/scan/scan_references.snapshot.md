## Resource

```python
from pprint import pprint

import example_references
from ordeq._resolve import _resolve_packages_to_modules
from ordeq._scan import scan

nodes, ios = scan(*_resolve_packages_to_modules(example_references))
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
[(('example_references.io_references',
   'test_io'),
  Input(id=ID1)),
 (('example_references.io_references',
   'nested_test_io'),
  Input(id=ID2)),
 (('example_references.io_references',
   'world'),
  Literal('World!')),
 (('example_references.io_references',
   'named_test_io'),
  Input(id=ID3)),
 (('example_references.io_references',
   'named_nested_test_io'),
  Input(id=ID4))]

```