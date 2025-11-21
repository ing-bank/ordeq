## Resource

```python
from pprint import pprint

import example_references
from ordeq._resolve import _resolve_packages_to_modules
from ordeq._scan import scan

nodes, ios = scan(*_resolve_packages_to_modules(example_references))
print("Nodes:")
pprint(nodes, width=200)
print("IOs:")
pprint(list(ios.values()), width=200)

```

## Output

```text
Nodes:
{}
IOs:
[('example_references.io_references', 'test_io'),
 ('example_references.io_references', 'nested_test_io'),
 ('example_references.io_references', 'world'),
 ('example_references.io_references', 'named_test_io'),
 ('example_references.io_references', 'named_nested_test_io')]

```