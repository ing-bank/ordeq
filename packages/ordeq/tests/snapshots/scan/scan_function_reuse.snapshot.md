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
[(FQN(module='example_function_reuse.nodes', name='a'),
  View(func=example_function_reuse.func_defs:print_input, inputs=[StringBuffer(_buffer=<_io.StringIO object at HASH1>)])),
 (FQN(module='example_function_reuse.nodes', name='b'),
  View(func=example_function_reuse.func_defs:print_input, inputs=[StringBuffer(_buffer=<_io.StringIO object at HASH2>)])),
 (FQN(module='example_function_reuse.nodes', name='c'),
  View(func=example_function_reuse.func_defs:print_input, inputs=[StringBuffer(_buffer=<_io.StringIO object at HASH3>)])),
 (FQN(module='example_function_reuse.nodes', name='d'),
  View(func=example_function_reuse.func_defs:print_input, inputs=[StringBuffer(_buffer=<_io.StringIO object at HASH4>)])),
 (FQN(module='example_function_reuse.nodes', name='pi'),
  View(module=example_function_reuse.nodes, name=pi, inputs=[StringBuffer(_buffer=<_io.StringIO object at HASH1>)]))]
IOs:
[(FQN(module='example_function_reuse.catalog', name='A'),
  StringBuffer(_buffer=<_io.StringIO object at HASH1>)),
 (FQN(module='example_function_reuse.nodes', name='A'),
  StringBuffer(_buffer=<_io.StringIO object at HASH1>)),
 (FQN(module='example_function_reuse.catalog', name='B'),
  StringBuffer(_buffer=<_io.StringIO object at HASH2>)),
 (FQN(module='example_function_reuse.nodes', name='B'),
  StringBuffer(_buffer=<_io.StringIO object at HASH2>)),
 (FQN(module='example_function_reuse.catalog', name='C'),
  StringBuffer(_buffer=<_io.StringIO object at HASH3>)),
 (FQN(module='example_function_reuse.catalog', name='D'),
  StringBuffer(_buffer=<_io.StringIO object at HASH4>))]

```