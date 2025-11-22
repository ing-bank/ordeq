## Resource

```python
import importlib
from pprint import pprint

from ordeq._resolve import (
    _resolve_refs_to_modules,
    _resolve_runnables_to_nodes,
    _resolve_runnables_to_nodes_and_ios,
)

runnables = [importlib.import_module("example_nested")]

modules = [mod.__name__ for mod in _resolve_refs_to_modules(*runnables)]
pprint(modules)

nodes, ios = _resolve_runnables_to_nodes_and_ios(*runnables)
pprint(nodes)
pprint(ios)

pprint(_resolve_runnables_to_nodes(*runnables))

```

## Output

```text
['example_nested',
 'example_nested.__main__',
 'example_nested.catalog',
 'example_nested.subpackage',
 'example_nested.subpackage.subsubpackage',
 'example_nested.subpackage.subsubpackage.hello',
 'example_nested.subpackage.subsubpackage.hello_relative']
[(('example_nested.__main__', 'world_relative'),
  Node(func=example_nested.subpackage.subsubpackage.hello_relative:world_relative, outputs=[StringBuffer(_buffer=<_io.StringIO object at HASH1>)])),
 (('example_nested.subpackage.subsubpackage.hello', 'world'),
  View(func=example_nested.subpackage.subsubpackage.hello:world)),
 (('example_nested.subpackage.subsubpackage.hello_relative', 'world_relative'),
  Node(func=example_nested.subpackage.subsubpackage.hello_relative:world_relative, outputs=[StringBuffer(_buffer=<_io.StringIO object at HASH1>)]))]
{'example_nested.catalog': {'message': StringBuffer(_buffer=<_io.StringIO object at HASH1>)},
 'example_nested.subpackage.subsubpackage.hello_relative': {'message': StringBuffer(_buffer=<_io.StringIO object at HASH1>)}}
[(('example_nested.__main__', 'world_relative'),
  Node(func=example_nested.subpackage.subsubpackage.hello_relative:world_relative, outputs=[StringBuffer(_buffer=<_io.StringIO object at HASH1>)])),
 (('example_nested.subpackage.subsubpackage.hello', 'world'),
  View(func=example_nested.subpackage.subsubpackage.hello:world)),
 (('example_nested.subpackage.subsubpackage.hello_relative', 'world_relative'),
  Node(func=example_nested.subpackage.subsubpackage.hello_relative:world_relative, outputs=[StringBuffer(_buffer=<_io.StringIO object at HASH1>)]))]

```