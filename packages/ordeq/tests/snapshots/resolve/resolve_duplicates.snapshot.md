## Resource

```python
import importlib

from ordeq._resolve import (
    _resolve_runnables_to_modules,
    _resolve_runnables_to_nodes,
    _resolve_runnables_to_nodes_and_ios,
)

runnables = [importlib.import_module("example_duplicates")]

modules = list(dict(_resolve_runnables_to_modules(*runnables)).keys())
print(modules)

nodes, ios = _resolve_runnables_to_nodes_and_ios(*runnables)
print(sorted(node.name for node in nodes))
print(dict(sorted(ios.items())))

print(sorted(node.name for node in _resolve_runnables_to_nodes(*runnables)))

```

## Output

```text
['example_duplicates', 'example_duplicates.file1', 'example_duplicates.file2']
['example_duplicates.file1:foo', 'example_duplicates.file2:foo']
{('example_duplicates.file1', 'x_value'): Literal(3), ('example_duplicates.file1', 'y_value'): IO(idx=ID1), ('example_duplicates.file2', 'x_value'): Literal(3), ('example_duplicates.file2', 'y_value'): IO(idx=ID2)}
['example_duplicates.file1:foo', 'example_duplicates.file2:foo']

```