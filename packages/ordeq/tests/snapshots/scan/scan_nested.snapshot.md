## Resource

```python
from pprint import pprint

import example_nested
from ordeq._resolve import _resolve_packages_to_modules
from ordeq._scan import scan

nodes, ios = scan(*_resolve_packages_to_modules(example_nested))
print("Nodes:")
pprint(nodes)
print("IOs:")
pprint(ios, width=40)

```

## Output

```text
Nodes:
[(('example_nested.__main__', 'world_relative'),
  Node(module=example_nested.subpackage.subsubpackage.hello_relative, name=world_relative, outputs=[StringBuffer(_buffer=<_io.StringIO object at HASH1>)])),
 (('example_nested.subpackage.subsubpackage.hello_relative', 'world_relative'),
  Node(module=example_nested.subpackage.subsubpackage.hello_relative, name=world_relative, outputs=[StringBuffer(_buffer=<_io.StringIO object at HASH1>)])),
 (('example_nested.subpackage.subsubpackage.hello', 'world'),
  View(func=example_nested.subpackage.subsubpackage.hello:world))]
IOs:
[(('example_nested.catalog', 'message'),
  StringBuffer(_buffer=<_io.StringIO object at HASH1>)),
 (('example_nested.subpackage.subsubpackage.hello_relative',
   'message'),
  StringBuffer(_buffer=<_io.StringIO object at HASH1>))]

```