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
[(FQN(module='example_references.io_references', name='test_io'),
  Input(id=ID1)),
 (FQN(module='example_references.io_references', name='nested_test_io'),
  Input(id=ID2)),
 (FQN(module='example_references.io_references', name='world'),
  Input(id=ID3)),
 (FQN(module='example_references.io_references', name='named_test_io'),
  Input(id=ID4)),
 (FQN(module='example_references.io_references', name='named_nested_test_io'),
  Input(id=ID5))]

```