## Resource

```python
import importlib

from ordeq._resolve import (
    _resolve_runnables_to_modules,
    _resolve_runnables_to_nodes,
    _resolve_runnables_to_nodes_and_ios,
)

runnables = [importlib.import_module("examples.function_reuse")]

modules = list(dict(_resolve_runnables_to_modules(*runnables)).keys())
print(modules)

nodes, ios = _resolve_runnables_to_nodes_and_ios(*runnables)
print(sorted(node.name for node in nodes))
print(dict(sorted(ios.items())))

print(sorted(node.name for node in _resolve_runnables_to_nodes(*runnables)))

```

## Output

```text
['examples.function_reuse', 'examples.function_reuse.catalog', 'examples.function_reuse.func_defs', 'examples.function_reuse.nodes']
['examples.function_reuse.func_defs:print_input', 'examples.function_reuse.func_defs:print_input', 'examples.function_reuse.func_defs:print_input', 'examples.function_reuse.func_defs:print_input', 'examples.function_reuse.nodes:pi']
{('examples.function_reuse.catalog', 'A'): StringBuffer(_buffer=<_io.StringIO object at HASH1>), ('examples.function_reuse.catalog', 'B'): StringBuffer(_buffer=<_io.StringIO object at HASH2>), ('examples.function_reuse.catalog', 'C'): StringBuffer(_buffer=<_io.StringIO object at HASH3>), ('examples.function_reuse.catalog', 'D'): StringBuffer(_buffer=<_io.StringIO object at HASH4>), ('examples.function_reuse.catalog', 'another_name'): StringBuffer(_buffer=<_io.StringIO object at HASH1>), ('examples.function_reuse.nodes', 'A'): StringBuffer(_buffer=<_io.StringIO object at HASH1>), ('examples.function_reuse.nodes', 'B'): StringBuffer(_buffer=<_io.StringIO object at HASH2>)}
['examples.function_reuse.func_defs:print_input', 'examples.function_reuse.func_defs:print_input', 'examples.function_reuse.func_defs:print_input', 'examples.function_reuse.func_defs:print_input', 'examples.function_reuse.nodes:pi']

```

## Logging

```text
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'examples.function_reuse.func_defs:print_input'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'examples.function_reuse.func_defs:print_input'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'examples.function_reuse.func_defs:print_input'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'examples.function_reuse.func_defs:print_input'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'examples.function_reuse.func_defs:print_input'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'examples.function_reuse.nodes:pi'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'examples.function_reuse.func_defs:print_input'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'examples.function_reuse.func_defs:print_input'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'examples.function_reuse.func_defs:print_input'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 

```