## Resource

```python
from pprint import pprint

import example_function_reuse
from ordeq._resolve import _resolve_packages_to_modules
from ordeq._scan import scan

nodes, ios = scan(*_resolve_packages_to_modules(example_function_reuse))
print("Nodes:")
pprint(nodes)
print("IOs:")
pprint(ios, width=40)

```

## Output

```text
Nodes:
[(('example_function_reuse.nodes', 'a'),
  View(func=<function print_input at HASH1>, inputs=[StringBuffer(_buffer=<_io.StringIO object at HASH2>)])),
 (('example_function_reuse.nodes', 'b'),
  View(func=<function print_input at HASH3>, inputs=[StringBuffer(_buffer=<_io.StringIO object at HASH4>)])),
 (('example_function_reuse.nodes', 'c'),
  View(func=<function print_input at HASH5>, inputs=[StringBuffer(_buffer=<_io.StringIO object at HASH6>)])),
 (('example_function_reuse.nodes', 'd'),
  View(func=<function print_input at HASH7>, inputs=[StringBuffer(_buffer=<_io.StringIO object at HASH8>)])),
 (('example_function_reuse.nodes', 'pi'),
  View(func=<function pi at HASH9>, inputs=[StringBuffer(_buffer=<_io.StringIO object at HASH2>)]))]
IOs:
[(('example_function_reuse.catalog',
   'A'),
  StringBuffer(_buffer=<_io.StringIO object at HASH2>)),
 (('example_function_reuse.nodes', 'A'),
  StringBuffer(_buffer=<_io.StringIO object at HASH2>)),
 (('example_function_reuse.catalog',
   'B'),
  StringBuffer(_buffer=<_io.StringIO object at HASH4>)),
 (('example_function_reuse.nodes', 'B'),
  StringBuffer(_buffer=<_io.StringIO object at HASH4>)),
 (('example_function_reuse.catalog',
   'C'),
  StringBuffer(_buffer=<_io.StringIO object at HASH6>)),
 (('example_function_reuse.catalog',
   'D'),
  StringBuffer(_buffer=<_io.StringIO object at HASH8>))]

```