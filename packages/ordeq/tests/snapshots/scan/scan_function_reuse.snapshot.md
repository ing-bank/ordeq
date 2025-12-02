## Resource

```python
from pprint import pp

import example_function_reuse
from ordeq._resolve import _resolve_packages_to_modules
from ordeq._scan import _scan_fqns

nodes, ios = _scan_fqns(*_resolve_packages_to_modules(example_function_reuse))
print("Nodes:")
pp(nodes, width=40)
print("IOs:")
pp(list(ios.values()), width=40)

```

## Output

```text
Nodes:
{View(func=example_function_reuse.func_defs:print_input, inputs=[StringBuffer(_buffer=<_io.StringIO object at HASH1>)]): [FQN(module='example_function_reuse.nodes', name='a')],
 View(func=example_function_reuse.func_defs:print_input, inputs=[StringBuffer(_buffer=<_io.StringIO object at HASH2>)]): [FQN(module='example_function_reuse.nodes', name='b')],
 View(func=example_function_reuse.func_defs:print_input, inputs=[StringBuffer(_buffer=<_io.StringIO object at HASH3>)]): [FQN(module='example_function_reuse.nodes', name='c')],
 View(func=example_function_reuse.func_defs:print_input, inputs=[StringBuffer(_buffer=<_io.StringIO object at HASH4>)]): [FQN(module='example_function_reuse.nodes', name='d')],
 View(module=example_function_reuse.nodes, name=pi, inputs=[StringBuffer(_buffer=<_io.StringIO object at HASH1>)]): [FQN(module='example_function_reuse.nodes', name='pi')]}
IOs:
[[FQN(module='example_function_reuse.catalog', name='A'),
  FQN(module='example_function_reuse.nodes', name='A')],
 [FQN(module='example_function_reuse.catalog', name='B'),
  FQN(module='example_function_reuse.nodes', name='B')],
 [FQN(module='example_function_reuse.catalog', name='C')],
 [FQN(module='example_function_reuse.catalog', name='D')]]

```