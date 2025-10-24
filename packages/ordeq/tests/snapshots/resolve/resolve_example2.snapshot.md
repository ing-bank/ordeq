## Resource

```python
from ordeq._resolve import (
    _resolve_runnables_to_modules,
    _resolve_runnables_to_nodes,
    _resolve_runnables_to_nodes_and_ios,
)
import importlib

runnables = [
    importlib.import_module("example2"),
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
['example2', 'example2.catalog', 'example2.nodes']
['example2.nodes:transform_input_2']
{('example2.catalog', 'TestInput2'): Input(idx=ID1), ('example2.catalog', 'TestOutput2'): Output(idx=ID2), ('example2.nodes', 'TestInput2'): Input(idx=ID1), ('example2.nodes', 'TestOutput2'): Output(idx=ID2)}
['example2.nodes:transform_input_2']

```