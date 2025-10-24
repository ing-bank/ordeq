## Resource:
```python
from ordeq._resolve import (
    _resolve_runnables_to_modules,
    _resolve_runnables_to_nodes,
    _resolve_runnables_to_nodes_and_ios,
)
import importlib

runnables = [
    importlib.import_module("function_reuse.nodes"),
]

modules = list(dict(_resolve_runnables_to_modules(*runnables)).keys())
print(modules)

nodes, ios = _resolve_runnables_to_nodes_and_ios(*runnables)
print(list(sorted(node.name for node in nodes)))
print(dict(sorted(ios.items())))

print(list(sorted(node.name for node in _resolve_runnables_to_nodes(*runnables))))

```

## Output:
```text
['function_reuse.nodes']
['function_reuse.func_defs:print_input', 'function_reuse.func_defs:print_input', 'function_reuse.func_defs:print_input', 'function_reuse.func_defs:print_input', 'function_reuse.nodes:pi']
{('function_reuse.nodes', 'A'): StringBuffer(_buffer=<_io.StringIO object at HASH1>), ('function_reuse.nodes', 'B'): StringBuffer(_buffer=<_io.StringIO object at HASH2>)}
['function_reuse.func_defs:print_input', 'function_reuse.func_defs:print_input', 'function_reuse.func_defs:print_input', 'function_reuse.func_defs:print_input', 'function_reuse.nodes:pi']

```