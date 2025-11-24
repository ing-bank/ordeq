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
[(FQN(module='example_1.nodes', name='world'),
  Node(func=example_1.nodes:world, inputs=[StringBuffer(_buffer=<_io.StringIO object at HASH1>)], outputs=[StringBuffer(_buffer=<_io.StringIO object at HASH2>)])),
 (FQN(module='example_1.pipeline', name='transform_input'),
  Node(func=example_1.pipeline:transform_input, inputs=[Input(id=ID1)], outputs=[Output(id=ID2)])),
 (FQN(module='example_1.pipeline', name='transform_mock_input'),
  Node(func=example_1.pipeline:transform_mock_input, inputs=[StringBuffer(_buffer=<_io.StringIO object at HASH3>)], outputs=[StringBuffer(_buffer=<_io.StringIO object at HASH4>)])),
 (FQN(module='example_1.wrapped_io', name='hello'),
  Node(func=example_1.wrapped_io:hello, inputs=[NameGenerator(name='John')], outputs=[SayHello(name=NameGenerator(name='John'), writer=(NamePrinter(),))])),
 (FQN(module='example_1.wrapped_io', name='print_message'),
  Node(func=example_1.wrapped_io:print_message, inputs=[SayHello(name=NameGenerator(name='John'), writer=(NamePrinter(),))], outputs=[NamePrinter()]))]
IOs:
[(FQN(module='example_1.catalog', name='Hello'),
  StringBuffer(_buffer=<_io.StringIO object at HASH3>)),
 (FQN(module='example_1.pipeline', name='Hello'),
  StringBuffer(_buffer=<_io.StringIO object at HASH3>)),
 (FQN(module='example_1.catalog', name='World'),
  StringBuffer(_buffer=<_io.StringIO object at HASH4>)),
 (FQN(module='example_1.pipeline', name='World'),
  StringBuffer(_buffer=<_io.StringIO object at HASH4>)),
 (FQN(module='example_1.catalog', name='TestInput'),
  Input(id=ID1)),
 (FQN(module='example_1.pipeline', name='TestInput'),
  Input(id=ID1)),
 (FQN(module='example_1.catalog', name='TestOutput'),
  Output(id=ID2)),
 (FQN(module='example_1.pipeline', name='TestOutput'),
  Output(id=ID2)),
 (FQN(module='example_1.nodes', name='x'),
  StringBuffer(_buffer=<_io.StringIO object at HASH1>)),
 (FQN(module='example_1.nodes', name='y'),
  StringBuffer(_buffer=<_io.StringIO object at HASH2>)),
 (FQN(module='example_1.wrapped_io', name='name_generator'),
  NameGenerator(name='John')),
 (FQN(module='example_1.wrapped_io', name='name_printer'),
  NamePrinter()),
 (FQN(module='example_1.wrapped_io', name='message'),
  SayHello(name=NameGenerator(name='John'),
           writer=(NamePrinter(),)))]

```