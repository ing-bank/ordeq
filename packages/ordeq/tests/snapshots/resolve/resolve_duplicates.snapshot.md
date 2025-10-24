## Resource

```python
from ordeq._resolve import (
    _resolve_runnables_to_modules,
    _resolve_runnables_to_nodes,
    _resolve_runnables_to_nodes_and_ios,
)
import importlib

runnables = [
    importlib.import_module("duplicates"),
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
['duplicates', 'duplicates.file1', 'duplicates.file2']
['duplicates.file1:foo', 'duplicates.file2:foo']
{('duplicates.file1', 'x_value'): Literal(3), ('duplicates.file1', 'y_value'): IO(idx=ID1), ('duplicates.file2', 'x_value'): Literal(3), ('duplicates.file2', 'y_value'): IO(idx=ID2)}
['duplicates.file1:foo', 'duplicates.file2:foo']

```