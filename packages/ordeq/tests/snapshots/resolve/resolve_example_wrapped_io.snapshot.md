## Resource

```python
from ordeq._resolve import (
    _resolve_runnables_to_modules,
    _resolve_runnables_to_nodes,
    _resolve_runnables_to_nodes_and_ios,
)
import importlib

runnables = [
    importlib.import_module("example.wrapped_io"),
]

modules = list(dict(_resolve_runnables_to_modules(*runnables)).keys())
print(modules)

nodes, ios = _resolve_runnables_to_nodes_and_ios(*runnables)
print(dict(sorted(nodes.items())))
print(dict(sorted(ios.items())))

print(dict(sorted(_resolve_runnables_to_nodes(*runnables).items())))

```

## Output

```text
['example.wrapped_io']
{('example.wrapped_io', 'hello'): Node(name=example.wrapped_io:hello, inputs=[NameGenerator(name='John')], outputs=[SayHello(name=NameGenerator(name='John'), writer=(NamePrinter(),))]), ('example.wrapped_io', 'print_message'): Node(name=example.wrapped_io:print_message, inputs=[SayHello(name=NameGenerator(name='John'), writer=(NamePrinter(),))], outputs=[NamePrinter()])}
{('example.wrapped_io', 'message'): SayHello(name=NameGenerator(name='John'), writer=(NamePrinter(),)), ('example.wrapped_io', 'name_generator'): NameGenerator(name='John'), ('example.wrapped_io', 'name_printer'): NamePrinter()}
{('example.wrapped_io', 'hello'): Node(name=example.wrapped_io:hello, inputs=[NameGenerator(name='John')], outputs=[SayHello(name=NameGenerator(name='John'), writer=(NamePrinter(),))]), ('example.wrapped_io', 'print_message'): Node(name=example.wrapped_io:print_message, inputs=[SayHello(name=NameGenerator(name='John'), writer=(NamePrinter(),))], outputs=[NamePrinter()])}

```