## Resource

```python
import importlib

from ordeq._resolve import (
    _resolve_runnables_to_modules,
    _resolve_runnables_to_nodes,
    _resolve_runnables_to_nodes_and_ios,
)

runnables = [importlib.import_module("examples.example")]

modules = list(dict(_resolve_runnables_to_modules(*runnables)).keys())
print(modules)

nodes, ios = _resolve_runnables_to_nodes_and_ios(*runnables)
print(sorted(node.name for node in nodes))
print(dict(sorted(ios.items())))

print(sorted(node.name for node in _resolve_runnables_to_nodes(*runnables)))

```

## Output

```text
['examples.example', 'examples.example.catalog', 'examples.example.hooks', 'examples.example.nodes', 'examples.example.pipeline', 'examples.example.wrapped_io']
['examples.example.nodes:world', 'examples.example.pipeline:transform_input', 'examples.example.pipeline:transform_mock_input', 'examples.example.wrapped_io:hello', 'examples.example.wrapped_io:print_message']
{('examples.example.catalog', 'Hello'): StringBuffer(_buffer=<_io.StringIO object at HASH1>), ('examples.example.catalog', 'TestInput'): Input(idx=ID1), ('examples.example.catalog', 'TestOutput'): Output(idx=ID2), ('examples.example.catalog', 'World'): StringBuffer(_buffer=<_io.StringIO object at HASH2>), ('examples.example.nodes', 'x'): StringBuffer(_buffer=<_io.StringIO object at HASH3>), ('examples.example.nodes', 'y'): StringBuffer(_buffer=<_io.StringIO object at HASH4>), ('examples.example.pipeline', 'Hello'): StringBuffer(_buffer=<_io.StringIO object at HASH1>), ('examples.example.pipeline', 'TestInput'): Input(idx=ID1), ('examples.example.pipeline', 'TestOutput'): Output(idx=ID2), ('examples.example.pipeline', 'World'): StringBuffer(_buffer=<_io.StringIO object at HASH2>), ('examples.example.wrapped_io', 'message'): SayHello(name=NameGenerator(name='John'), writer=(NamePrinter(),)), ('examples.example.wrapped_io', 'name_generator'): NameGenerator(name='John'), ('examples.example.wrapped_io', 'name_printer'): NamePrinter()}
['examples.example.nodes:world', 'examples.example.pipeline:transform_input', 'examples.example.pipeline:transform_mock_input', 'examples.example.wrapped_io:hello', 'examples.example.wrapped_io:print_message']

```