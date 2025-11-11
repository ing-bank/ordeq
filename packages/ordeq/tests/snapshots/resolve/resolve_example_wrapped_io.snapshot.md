## Resource

```python
import importlib
from pprint import pprint

from ordeq._resolve import (
    _resolve_refs_to_modules,
    _resolve_runnables_to_nodes,
    _resolve_runnables_to_nodes_and_ios,
)

runnables = [importlib.import_module("example_1.wrapped_io")]

modules = [mod.__name__ for mod in _resolve_refs_to_modules(*runnables)]
pprint(modules)

nodes, ios = _resolve_runnables_to_nodes_and_ios(*runnables)
pprint(sorted(node.name for node in nodes))
pprint(dict(sorted(ios.items())))

pprint(sorted(node.name for node in _resolve_runnables_to_nodes(*runnables)))

```

## Output

```text
['example_1.wrapped_io']
['example_1.wrapped_io:hello', 'example_1.wrapped_io:print_message']
{'example_1.wrapped_io': {'message': SayHello(name=NameGenerator(name='John'),
                                              writer=(NamePrinter(),)),
                          'name_generator': NameGenerator(name='John'),
                          'name_printer': NamePrinter()}}
['example_1.wrapped_io:hello', 'example_1.wrapped_io:print_message']

```