## Resource

```python
import importlib
from pprint import pprint

from ordeq._resolve import (
    _resolve_refs_to_modules,
    _resolve_runnables_to_nodes,
    _resolve_runnables_to_nodes_and_ios,
)

runnables = [importlib.import_module("example_3")]

modules = [mod.__name__ for mod in _resolve_refs_to_modules(*runnables)]
pprint(modules)

nodes, ios = _resolve_runnables_to_nodes_and_ios(*runnables)
pprint(nodes)
pprint(ios)

pprint(_resolve_runnables_to_nodes(*runnables))

```

## Output

```text
['example_3', 'example_3.func_defs', 'example_3.nodes']
[(('example_3.nodes', 'f1'), View(func=<function hello at HASH1>)),
 (('example_3.nodes', 'f2'), View(func=<function hello at HASH2>))]
{}
[(('example_3.nodes', 'f1'), View(func=<function hello at HASH1>)),
 (('example_3.nodes', 'f2'), View(func=<function hello at HASH2>))]

```