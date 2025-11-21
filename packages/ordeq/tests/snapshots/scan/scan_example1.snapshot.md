## Resource

```python
from pprint import pprint

import example_1
from ordeq._resolve import _resolve_packages_to_modules
from ordeq._scan import scan

nodes, ios = scan(*_resolve_packages_to_modules(example_1))
print("Nodes:")
pprint(list(nodes.values()), width=200)
print("IOs:")
pprint(list(ios.values()), width=200)

```

## Output

```text
Nodes:
[('example_1.nodes', 'world'), ('example_1.pipeline', 'transform_input'), ('example_1.pipeline', 'transform_mock_input'), ('example_1.wrapped_io', 'hello'), ('example_1.wrapped_io', 'print_message')]
IOs:
[('example_1.pipeline', 'Hello'),
 ('example_1.pipeline', 'World'),
 ('example_1.pipeline', 'TestInput'),
 ('example_1.pipeline', 'TestOutput'),
 ('example_1.nodes', 'x'),
 ('example_1.nodes', 'y'),
 ('example_1.wrapped_io', 'name_generator'),
 ('example_1.wrapped_io', 'name_printer'),
 ('example_1.wrapped_io', 'message')]

```