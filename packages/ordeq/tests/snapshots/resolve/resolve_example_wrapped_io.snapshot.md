## Resource

```python
import importlib

from ordeq._resolve import (
    _resolve_runnables_to_modules,
    _resolve_runnables_to_nodes,
    _resolve_runnables_to_nodes_and_ios,
)

runnables = [importlib.import_module("example_1.wrapped_io")]

modules = list(dict(_resolve_runnables_to_modules(*runnables)).keys())
print(modules)

nodes, ios = _resolve_runnables_to_nodes_and_ios(*runnables)
print(sorted(node.name for node in nodes))
print(dict(sorted(ios.items())))

print(sorted(node.name for node in _resolve_runnables_to_nodes(*runnables)))

```

## Output

```text
['example_1.wrapped_io']
['example_1.wrapped_io:hello', 'example_1.wrapped_io:print_message']
{('example_1.wrapped_io', 'message'): SayHello(name=NameGenerator(name='John'), writer=(NamePrinter(),)), ('example_1.wrapped_io', 'name_generator'): NameGenerator(name='John'), ('example_1.wrapped_io', 'name_printer'): NamePrinter()}
['example_1.wrapped_io:hello', 'example_1.wrapped_io:print_message']

```