## Resource:
```python
from ordeq._resolve import (
    _resolve_runnables_to_modules,
    _resolve_runnables_to_nodes,
    _resolve_runnables_to_nodes_and_ios,
)
import importlib

runnables = [
    importlib.import_module("nested"),
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
['nested', 'nested.subpackage', 'nested.subpackage.subsubpackage', 'nested.subpackage.subsubpackage.hello']
['nested.subpackage.subsubpackage.hello:world']
{}
['nested.subpackage.subsubpackage.hello:world']

```