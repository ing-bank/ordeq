## Resource

```python
from ordeq._resolve import (
    _resolve_runnables_to_modules,
    _resolve_runnables_to_nodes,
    _resolve_runnables_to_nodes_and_ios,
)
import importlib

runnables = [
    importlib.import_module("example"),
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
['example', 'example.catalog', 'example.hooks', 'example.nodes', 'example.pipeline', 'example.wrapped_io']
['example.nodes:world', 'example.pipeline:transform_input', 'example.pipeline:transform_mock_input', 'example.wrapped_io:hello', 'example.wrapped_io:print_message']
{('example.catalog', 'Hello'): StringBuffer(_buffer=<_io.StringIO object at HASH1>), ('example.catalog', 'TestInput'): Input(idx=ID1), ('example.catalog', 'TestOutput'): Output(idx=ID2), ('example.catalog', 'World'): StringBuffer(_buffer=<_io.StringIO object at HASH2>), ('example.nodes', 'x'): StringBuffer(_buffer=<_io.StringIO object at HASH3>), ('example.nodes', 'y'): StringBuffer(_buffer=<_io.StringIO object at HASH4>), ('example.pipeline', 'Hello'): StringBuffer(_buffer=<_io.StringIO object at HASH1>), ('example.pipeline', 'TestInput'): Input(idx=ID1), ('example.pipeline', 'TestOutput'): Output(idx=ID2), ('example.pipeline', 'World'): StringBuffer(_buffer=<_io.StringIO object at HASH2>), ('example.wrapped_io', 'message'): SayHello(name=NameGenerator(name='John'), writer=(NamePrinter(),)), ('example.wrapped_io', 'name_generator'): NameGenerator(name='John'), ('example.wrapped_io', 'name_printer'): NamePrinter()}
['example.nodes:world', 'example.pipeline:transform_input', 'example.pipeline:transform_mock_input', 'example.wrapped_io:hello', 'example.wrapped_io:print_message']

```