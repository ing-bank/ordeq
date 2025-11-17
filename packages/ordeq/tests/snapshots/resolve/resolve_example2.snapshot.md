## Resource

```python
import importlib
from pprint import pprint

from ordeq._resolve import (
    _resolve_refs_to_modules,
    _resolve_runnables_to_nodes,
    _resolve_runnables_to_nodes_and_ios,
)

runnables = [importlib.import_module("example_2")]

modules = [mod.__name__ for mod in _resolve_refs_to_modules(*runnables)]
pprint(modules)

nodes, ios = _resolve_runnables_to_nodes_and_ios(*runnables)
pprint(sorted(node.name for node in nodes))
pprint(dict(sorted(ios.items())))

pprint(sorted(node.name for node in _resolve_runnables_to_nodes(*runnables)))

```

## Output

```text
['example_2', 'example_2.catalog', 'example_2.nodes']
['example_2.nodes:transform_input_2']
{'example_2.catalog': {'TestInput2': Input(id=ID1),
                       'TestOutput2': Output(id=ID2)},
 'example_2.nodes': {'TestInput2': Input(id=ID1),
                     'TestOutput2': Output(id=ID2)}}
['example_2.nodes:transform_input_2']

```