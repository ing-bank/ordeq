## Resource

```python
import importlib

from ordeq._resolve import (
    _resolve_runnables_to_modules,
    _resolve_runnables_to_nodes,
    _resolve_runnables_to_nodes_and_ios,
)

runnables = [importlib.import_module("example_2")]

modules = list(dict(_resolve_runnables_to_modules(*runnables)).keys())
print(modules)

nodes, ios = _resolve_runnables_to_nodes_and_ios(*runnables)
print(sorted(node.name for node in nodes))
print(dict(sorted(ios.items())))

print(sorted(node.name for node in _resolve_runnables_to_nodes(*runnables)))

```

## Output

```text
['example_2', 'example_2.catalog', 'example_2.nodes']
['example_2.nodes:transform_input_2']
{('example_2.catalog', 'TestInput2'): Input(idx=ID1), ('example_2.catalog', 'TestOutput2'): Output(idx=ID2), ('example_2.nodes', 'TestInput2'): Input(idx=ID1), ('example_2.nodes', 'TestOutput2'): Output(idx=ID2)}
['example_2.nodes:transform_input_2']

```