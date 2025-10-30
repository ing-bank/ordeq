## Resource

```python
import importlib

from ordeq._resolve import (
    _resolve_runnables_to_modules,
    _resolve_runnables_to_nodes,
    _resolve_runnables_to_nodes_and_ios,
)

runnables = [importlib.import_module("example_function_reuse.nodes")]

modules = list(dict(_resolve_runnables_to_modules(*runnables)).keys())
print(modules)

nodes, ios = _resolve_runnables_to_nodes_and_ios(*runnables)
print(sorted(node.name for node in nodes))
print(dict(sorted(ios.items())))

print(sorted(node.name for node in _resolve_runnables_to_nodes(*runnables)))

```

## Output

```text
['example_function_reuse.nodes']
['example_function_reuse.func_defs:print_input', 'example_function_reuse.func_defs:print_input', 'example_function_reuse.func_defs:print_input', 'example_function_reuse.func_defs:print_input', 'example_function_reuse.nodes:pi']
{('example_function_reuse.nodes', 'A'): StringBuffer(_buffer=<_io.StringIO object at HASH1>), ('example_function_reuse.nodes', 'B'): StringBuffer(_buffer=<_io.StringIO object at HASH2>)}
['example_function_reuse.func_defs:print_input', 'example_function_reuse.func_defs:print_input', 'example_function_reuse.func_defs:print_input', 'example_function_reuse.func_defs:print_input', 'example_function_reuse.nodes:pi']

```