## Resource

```python
from ordeq._resolve import (
    _resolve_runnables_to_modules,
    _resolve_runnables_to_nodes,
    _resolve_runnables_to_nodes_and_ios,
)
import importlib

runnables = [
    importlib.import_module("function_reuse"),
]

modules = list(dict(_resolve_runnables_to_modules(*runnables)).keys())
print(modules)

nodes, ios = _resolve_runnables_to_nodes_and_ios(*runnables)
print(list(sorted(node.name for node in nodes)))
print(dict(sorted(ios.items())))

print(list(sorted(node.name for node in _resolve_runnables_to_nodes(*runnables))))

```

## Output

```text
['function_reuse', 'function_reuse.catalog', 'function_reuse.func_defs', 'function_reuse.nodes']
['function_reuse.func_defs:print_input', 'function_reuse.func_defs:print_input', 'function_reuse.func_defs:print_input', 'function_reuse.func_defs:print_input', 'function_reuse.nodes:pi']
{('function_reuse.catalog', 'A'): StringBuffer(_buffer=<_io.StringIO object at HASH1>), ('function_reuse.catalog', 'B'): StringBuffer(_buffer=<_io.StringIO object at HASH2>), ('function_reuse.catalog', 'C'): StringBuffer(_buffer=<_io.StringIO object at HASH3>), ('function_reuse.catalog', 'D'): StringBuffer(_buffer=<_io.StringIO object at HASH4>), ('function_reuse.catalog', 'another_name'): StringBuffer(_buffer=<_io.StringIO object at HASH1>), ('function_reuse.nodes', 'A'): StringBuffer(_buffer=<_io.StringIO object at HASH1>), ('function_reuse.nodes', 'B'): StringBuffer(_buffer=<_io.StringIO object at HASH2>)}
['function_reuse.func_defs:print_input', 'function_reuse.func_defs:print_input', 'function_reuse.func_defs:print_input', 'function_reuse.func_defs:print_input', 'function_reuse.nodes:pi']

```

## Logging

```text
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'function_reuse.func_defs:print_input'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'function_reuse.func_defs:print_input'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'function_reuse.func_defs:print_input'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'function_reuse.func_defs:print_input'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'function_reuse.func_defs:print_input'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'function_reuse.nodes:pi'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'function_reuse.func_defs:print_input'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'function_reuse.func_defs:print_input'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'function_reuse.func_defs:print_input'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 

```