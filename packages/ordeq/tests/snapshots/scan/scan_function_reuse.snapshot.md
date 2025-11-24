## Resource

```python
from pprint import pprint

import example_function_reuse
from ordeq._resolve import _resolve_packages_to_modules
from ordeq._scan import _scan_fqns

nodes, ios = _scan_fqns(*_resolve_packages_to_modules(example_function_reuse))
print("Nodes:")
pprint(sorted(nodes, key=lambda n: n.ref), width=40)
print("IOs:")
pprint(list(ios.values()), width=40)

```

## Output

```text
Nodes:
[View(func=example_function_reuse.func_defs:print_input, inputs=[StringBuffer(_buffer=<_io.StringIO object at HASH1>)]),
 View(func=example_function_reuse.func_defs:print_input, inputs=[StringBuffer(_buffer=<_io.StringIO object at HASH2>)]),
 View(func=example_function_reuse.func_defs:print_input, inputs=[StringBuffer(_buffer=<_io.StringIO object at HASH3>)]),
 View(func=example_function_reuse.func_defs:print_input, inputs=[StringBuffer(_buffer=<_io.StringIO object at HASH4>)]),
 View(module=example_function_reuse.nodes, name=pi, inputs=[StringBuffer(_buffer=<_io.StringIO object at HASH1>)])]
IOs:
[[FQN(module='example_function_reuse.catalog', name='A'),
  FQN(module='example_function_reuse.nodes', name='A')],
 [FQN(module='example_function_reuse.catalog', name='B'),
  FQN(module='example_function_reuse.nodes', name='B')],
 [FQN(module='example_function_reuse.catalog', name='C')],
 [FQN(module='example_function_reuse.catalog', name='D')]]

```

## Warnings

```text
UserWarning: Module 'example_function_reuse.catalog' already provided as runnable
UserWarning: Module 'example_function_reuse.func_defs' already provided as runnable
UserWarning: Module 'example_function_reuse.nodes' already provided as runnable
```