## Resource

```python
import importlib
from pprint import pprint

from ordeq._resolve import (
    _resolve_runnables_to_modules,
    _resolve_runnables_to_nodes,
    _resolve_runnables_to_nodes_and_ios,
)

runnables = [importlib.import_module("example_function_reuse")]

modules = [mod.__name__ for mod in _resolve_runnables_to_modules(*runnables)]
pprint(modules)

nodes, ios = _resolve_runnables_to_nodes_and_ios(*runnables)
pprint(sorted(node.name for node in nodes))
pprint(dict(sorted(ios.items())))

pprint(sorted(node.name for node in _resolve_runnables_to_nodes(*runnables)))

```

## Output

```text
['example_function_reuse',
 'example_function_reuse.catalog',
 'example_function_reuse.func_defs',
 'example_function_reuse.nodes']
['example_function_reuse.func_defs:print_input',
 'example_function_reuse.func_defs:print_input',
 'example_function_reuse.func_defs:print_input',
 'example_function_reuse.func_defs:print_input',
 'example_function_reuse.nodes:pi']
{'example_function_reuse.catalog': {'A': StringBuffer(_buffer=<_io.StringIO object at HASH1>),
                                    'B': StringBuffer(_buffer=<_io.StringIO object at HASH2>),
                                    'C': StringBuffer(_buffer=<_io.StringIO object at HASH3>),
                                    'D': StringBuffer(_buffer=<_io.StringIO object at HASH4>),
                                    'another_name': StringBuffer(_buffer=<_io.StringIO object at HASH1>)},
 'example_function_reuse.nodes': {'A': StringBuffer(_buffer=<_io.StringIO object at HASH1>),
                                  'B': StringBuffer(_buffer=<_io.StringIO object at HASH2>)}}
['example_function_reuse.func_defs:print_input',
 'example_function_reuse.func_defs:print_input',
 'example_function_reuse.func_defs:print_input',
 'example_function_reuse.func_defs:print_input',
 'example_function_reuse.nodes:pi']

```