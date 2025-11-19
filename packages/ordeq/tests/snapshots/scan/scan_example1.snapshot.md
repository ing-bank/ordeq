## Resource

```python
from pprint import pprint

import example_1
from ordeq._scan import scan

nodes, ios = scan(example_1)
print("Nodes:")
pprint(list(nodes.items()))
print("IOs:")
pprint(list(ios.values()), width=40)

```

## Output

```text
Nodes:
[(Node(name=example_1.nodes:world, inputs=[StringBuffer(_buffer=<_io.StringIO object at HASH1>)], outputs=[StringBuffer(_buffer=<_io.StringIO object at HASH2>)]),
  [('example_1.nodes', 'world')]),
 (Node(name=example_1.pipeline:transform_input, inputs=[Input(id=ID1)], outputs=[Output(id=ID2)]),
  [('example_1.pipeline', 'transform_input')]),
 (Node(name=example_1.pipeline:transform_mock_input, inputs=[StringBuffer(_buffer=<_io.StringIO object at HASH3>)], outputs=[StringBuffer(_buffer=<_io.StringIO object at HASH4>)]),
  [('example_1.pipeline', 'transform_mock_input')]),
 (Node(name=example_1.wrapped_io:hello, inputs=[NameGenerator(name='John')], outputs=[SayHello(name=NameGenerator(name='John'), writer=(NamePrinter(),))]),
  [('example_1.wrapped_io', 'hello')]),
 (Node(name=example_1.wrapped_io:print_message, inputs=[SayHello(name=NameGenerator(name='John'), writer=(NamePrinter(),))], outputs=[NamePrinter()]),
  [('example_1.wrapped_io', 'print_message')])]
IOs:
[[(('example_1.catalog', 'Hello'),
   StringBuffer(_buffer=<_io.StringIO object at HASH3>)),
  (('example_1.pipeline', 'Hello'),
   StringBuffer(_buffer=<_io.StringIO object at HASH3>))],
 [(('example_1.catalog', 'World'),
   StringBuffer(_buffer=<_io.StringIO object at HASH4>)),
  (('example_1.pipeline', 'World'),
   StringBuffer(_buffer=<_io.StringIO object at HASH4>))],
 [(('example_1.catalog', 'TestInput'),
   Input(id=ID1)),
  (('example_1.pipeline', 'TestInput'),
   Input(id=ID1))],
 [(('example_1.catalog', 'TestOutput'),
   Output(id=ID2)),
  (('example_1.pipeline', 'TestOutput'),
   Output(id=ID2))],
 [(('example_1.nodes', 'x'),
   StringBuffer(_buffer=<_io.StringIO object at HASH1>))],
 [(('example_1.nodes', 'y'),
   StringBuffer(_buffer=<_io.StringIO object at HASH2>))],
 [(('example_1.wrapped_io',
    'name_generator'),
   NameGenerator(name='John'))],
 [(('example_1.wrapped_io',
    'name_printer'),
   NamePrinter())],
 [(('example_1.wrapped_io', 'message'),
   SayHello(name=NameGenerator(name='John'),
            writer=(NamePrinter(),)))]]

```