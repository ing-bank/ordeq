## Resource

```python
import importlib
from pprint import pprint

from ordeq._resolve import (
    _resolve_runnables_to_modules,
    _resolve_runnables_to_nodes,
    _resolve_runnables_to_nodes_and_ios,
)

runnables = [importlib.import_module("example_nested")]

modules = [mod.__name__ for mod in _resolve_runnables_to_modules(*runnables)]
pprint(modules)

nodes, ios = _resolve_runnables_to_nodes_and_ios(*runnables)
pprint(sorted(node.name for node in nodes))
pprint(dict(sorted(ios.items())))

pprint(sorted(node.name for node in _resolve_runnables_to_nodes(*runnables)))

```

## Output

```text
['example_nested',
 'example_nested.subpackage',
 'example_nested.subpackage.subsubpackage',
 'example_nested.subpackage.subsubpackage.hello']
['example_nested.subpackage.subsubpackage.hello:world']
{}
['example_nested.subpackage.subsubpackage.hello:world']

```