## Resource

```python
import importlib

from ordeq._resolve import (
    _resolve_runnables_to_modules,
    _resolve_runnables_to_nodes,
    _resolve_runnables_to_nodes_and_ios,
)

runnables = [importlib.import_module("example3")]

modules = list(dict(_resolve_runnables_to_modules(*runnables)).keys())
print(modules)

nodes, ios = _resolve_runnables_to_nodes_and_ios(*runnables)
print(sorted(node.name for node in nodes))
print(dict(sorted(ios.items())))

print(sorted(node.name for node in _resolve_runnables_to_nodes(*runnables)))

```

## Output

```text
['example3', 'example3.func_defs', 'example3.nodes']
['example3.func_defs:hello', 'example3.func_defs:hello']
{}
['example3.func_defs:hello', 'example3.func_defs:hello']

```

## Logging

```text
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'example3.func_defs:hello'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'example3.func_defs:hello'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 

```