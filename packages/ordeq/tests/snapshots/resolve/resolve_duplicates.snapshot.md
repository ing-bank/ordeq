## Resource

```python
import importlib
from pprint import pprint

from ordeq._resolve import (
    _resolve_refs_to_modules,
    _resolve_runnables_to_nodes,
    _resolve_runnables_to_nodes_and_ios,
)

runnables = [importlib.import_module("example_duplicates")]

modules = [mod.__name__ for mod in _resolve_refs_to_modules(*runnables)]
pprint(modules)

nodes, ios = _resolve_runnables_to_nodes_and_ios(*runnables)
pprint(sorted(node.name for node in nodes))
pprint(dict(sorted(ios.items())))

pprint(sorted(node.name for node in _resolve_runnables_to_nodes(*runnables)))

```

## Output

```text
['example_duplicates',
 'example_duplicates.duplicate_io_name',
 'example_duplicates.duplicate_node_name',
 'example_duplicates.file1',
 'example_duplicates.file2']
['example_duplicates.duplicate_node_name:<lambda>',
 'example_duplicates.file1:foo',
 'example_duplicates.file2:foo']
{'example_duplicates.duplicate_io_name': {'x': Input(idx=ID1)},
 'example_duplicates.file1': {'x_value': Literal(3),
                              'y_value': IO(idx=ID2)},
 'example_duplicates.file2': {'x_value': Literal(3),
                              'y_value': IO(idx=ID3)}}
['example_duplicates.duplicate_node_name:<lambda>',
 'example_duplicates.file1:foo',
 'example_duplicates.file2:foo']

```