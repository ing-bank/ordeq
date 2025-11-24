## Resource

```python
from pprint import pprint

import example_1
from ordeq._resolve import _resolve_packages_to_modules
from ordeq._scan import scan

nodes, ios = scan(*_resolve_packages_to_modules(example_1))
print("Nodes:")
pprint(nodes)
print("IOs:")
pprint(ios, width=40)

```

## Output

```text
Nodes:
[(('example_1.nodes', 'world'),
  Node(module=example_1.nodes, name=world, inputs=[StringBuffer(_buffer=<_io.StringIO object at HASH1>)], outputs=[StringBuffer(_buffer=<_io.StringIO object at HASH2>)])),
 (('example_1.pipeline', 'transform_input'),
  Node(module=example_1.pipeline, name=transform_input, inputs=[Input(id=ID1)], outputs=[Output(id=ID2)])),
 (('example_1.pipeline', 'transform_mock_input'),
  Node(module=example_1.pipeline, name=transform_mock_input, inputs=[StringBuffer(_buffer=<_io.StringIO object at HASH3>)], outputs=[StringBuffer(_buffer=<_io.StringIO object at HASH4>)])),
 (('example_1.wrapped_io', 'hello'),
  Node(module=example_1.wrapped_io, name=hello, inputs=[NameGenerator(name='John')], outputs=[SayHello(name=NameGenerator(name='John'), writer=(NamePrinter(),))])),
 (('example_1.wrapped_io', 'print_message'),
  Node(module=example_1.wrapped_io, name=print_message, inputs=[SayHello(name=NameGenerator(name='John'), writer=(NamePrinter(),))], outputs=[NamePrinter()]))]
IOs:
[(('example_1.catalog', 'Hello'),
  StringBuffer(_buffer=<_io.StringIO object at HASH3>)),
 (('example_1.pipeline', 'Hello'),
  StringBuffer(_buffer=<_io.StringIO object at HASH3>)),
 (('example_1.catalog', 'World'),
  StringBuffer(_buffer=<_io.StringIO object at HASH4>)),
 (('example_1.pipeline', 'World'),
  StringBuffer(_buffer=<_io.StringIO object at HASH4>)),
 (('example_1.catalog', 'TestInput'),
  Input(id=ID1)),
 (('example_1.pipeline', 'TestInput'),
  Input(id=ID1)),
 (('example_1.catalog', 'TestOutput'),
  Output(id=ID2)),
 (('example_1.pipeline', 'TestOutput'),
  Output(id=ID2)),
 (('example_1.nodes', 'x'),
  StringBuffer(_buffer=<_io.StringIO object at HASH1>)),
 (('example_1.nodes', 'y'),
  StringBuffer(_buffer=<_io.StringIO object at HASH2>)),
 (('example_1.wrapped_io',
   'name_generator'),
  NameGenerator(name='John')),
 (('example_1.wrapped_io',
   'name_printer'),
  NamePrinter()),
 (('example_1.wrapped_io', 'message'),
  SayHello(name=NameGenerator(name='John'),
           writer=(NamePrinter(),)))]

```