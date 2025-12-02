## Resource

```python
import importlib
from pprint import pprint

from ordeq._resolve import (
    _resolve_refs_to_modules,
    _resolve_runnables_to_nodes,
    _resolve_runnables_to_nodes_and_ios,
)

runnables = [
    importlib.import_module("example_1"),
    importlib.import_module("example_1"),
    importlib.import_module("example_1"),
    importlib.import_module("example_1.wrapped_io"),
    importlib.import_module("example_1.nodes"),
]


modules = [mod.__name__ for mod in _resolve_refs_to_modules(*runnables)]
pprint(modules)

nodes, ios = _resolve_runnables_to_nodes_and_ios(*runnables)
pprint(nodes)
pprint(ios)

pprint(_resolve_runnables_to_nodes(*runnables))

```

## Output

```text
['example_1',
 'example_1.catalog',
 'example_1.hooks',
 'example_1.nodes',
 'example_1.pipeline',
 'example_1.wrapped_io',
 'example_1.wrapped_io',
 'example_1.nodes']
[Node(module=example_1.nodes, name=world, inputs=[IO(id=ID1)], outputs=[StringBuffer(_buffer=<_io.StringIO object at HASH1>)]),
 Node(module=example_1.pipeline, name=transform_input, inputs=[IO(id=ID2)], outputs=[Output(id=ID3)]),
 Node(module=example_1.pipeline, name=transform_mock_input, inputs=[IO(id=ID4)], outputs=[StringBuffer(_buffer=<_io.StringIO object at HASH2>)]),
 Node(module=example_1.wrapped_io, name=hello, inputs=[IO(id=ID5)], outputs=[SayHello(name=NameGenerator(name='John'), writer=(NamePrinter(),))]),
 Node(module=example_1.wrapped_io, name=print_message, inputs=[IO(id=ID6)], outputs=[NamePrinter()]),
 Node(module=example_1.wrapped_io, name=hello, inputs=[IO(id=ID5)], outputs=[SayHello(name=NameGenerator(name='John'), writer=(NamePrinter(),))]),
 Node(module=example_1.wrapped_io, name=print_message, inputs=[IO(id=ID6)], outputs=[NamePrinter()]),
 Node(module=example_1.nodes, name=world, inputs=[IO(id=ID1)], outputs=[StringBuffer(_buffer=<_io.StringIO object at HASH1>)])]
{'example_1.catalog': {'Hello': StringBuffer(_buffer=<_io.StringIO object at HASH3>),
                       'TestInput': Input(id=ID7),
                       'TestOutput': Output(id=ID3),
                       'World': StringBuffer(_buffer=<_io.StringIO object at HASH2>)},
 'example_1.nodes': {'x': StringBuffer(_buffer=<_io.StringIO object at HASH4>),
                     'y': StringBuffer(_buffer=<_io.StringIO object at HASH1>)},
 'example_1.pipeline': {'Hello': StringBuffer(_buffer=<_io.StringIO object at HASH3>),
                        'TestInput': Input(id=ID7),
                        'TestOutput': Output(id=ID3),
                        'World': StringBuffer(_buffer=<_io.StringIO object at HASH2>)},
 'example_1.wrapped_io': {'message': SayHello(name=NameGenerator(name='John'),
                                              writer=(NamePrinter(),)),
                          'name_generator': NameGenerator(name='John'),
                          'name_printer': NamePrinter()}}
[Node(module=example_1.nodes, name=world, inputs=[IO(id=ID1)], outputs=[StringBuffer(_buffer=<_io.StringIO object at HASH1>)]),
 Node(module=example_1.pipeline, name=transform_input, inputs=[IO(id=ID2)], outputs=[Output(id=ID3)]),
 Node(module=example_1.pipeline, name=transform_mock_input, inputs=[IO(id=ID4)], outputs=[StringBuffer(_buffer=<_io.StringIO object at HASH2>)]),
 Node(module=example_1.wrapped_io, name=hello, inputs=[IO(id=ID5)], outputs=[SayHello(name=NameGenerator(name='John'), writer=(NamePrinter(),))]),
 Node(module=example_1.wrapped_io, name=print_message, inputs=[IO(id=ID6)], outputs=[NamePrinter()]),
 Node(module=example_1.wrapped_io, name=hello, inputs=[IO(id=ID5)], outputs=[SayHello(name=NameGenerator(name='John'), writer=(NamePrinter(),))]),
 Node(module=example_1.wrapped_io, name=print_message, inputs=[IO(id=ID6)], outputs=[NamePrinter()]),
 Node(module=example_1.nodes, name=world, inputs=[IO(id=ID1)], outputs=[StringBuffer(_buffer=<_io.StringIO object at HASH1>)])]

```

## Warnings

```text
UserWarning: Module 'example_1' already provided as runnable
UserWarning: Module 'example_1' already provided as runnable
```