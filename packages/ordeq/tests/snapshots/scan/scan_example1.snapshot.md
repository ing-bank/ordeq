## Resource

```python
from pprint import pprint

import example_1
from ordeq._scan import _scan_fqns

nodes, ios = _scan_fqns(example_1)
print("Nodes:")
pprint(nodes)
print("IOs:")
pprint(list(ios.values()), width=40)

```

## Output

```text
Nodes:
{Node(module=example_1.pipeline, name=transform_input, inputs=[Input(id=ID1)], outputs=[Output(id=ID2)]): [FQN(module='example_1.pipeline', name='transform_input')],
 Node(module=example_1.wrapped_io, name=hello, inputs=[NameGenerator(name='John')], outputs=[SayHello(name=NameGenerator(name='John'), writer=(NamePrinter(),))]): [FQN(module='example_1.wrapped_io', name='hello')],
 Node(module=example_1.wrapped_io, name=print_message, inputs=[SayHello(name=NameGenerator(name='John'), writer=(NamePrinter(),))], outputs=[NamePrinter()]): [FQN(module='example_1.wrapped_io', name='print_message')],
 Node(module=example_1.nodes, name=world, inputs=[StringBuffer(_buffer=<_io.StringIO object at HASH1>)], outputs=[StringBuffer(_buffer=<_io.StringIO object at HASH2>)]): [FQN(module='example_1.nodes', name='world')],
 Node(module=example_1.pipeline, name=transform_mock_input, inputs=[StringBuffer(_buffer=<_io.StringIO object at HASH3>)], outputs=[StringBuffer(_buffer=<_io.StringIO object at HASH4>)]): [FQN(module='example_1.pipeline', name='transform_mock_input')]}
IOs:
[[FQN(module='example_1.catalog', name='Hello'),
  FQN(module='example_1.pipeline', name='Hello')],
 [FQN(module='example_1.catalog', name='World'),
  FQN(module='example_1.pipeline', name='World')],
 [FQN(module='example_1.catalog', name='TestInput'),
  FQN(module='example_1.pipeline', name='TestInput')],
 [FQN(module='example_1.catalog', name='TestOutput'),
  FQN(module='example_1.pipeline', name='TestOutput')],
 [FQN(module='example_1.nodes', name='x')],
 [FQN(module='example_1.nodes', name='y')],
 [FQN(module='example_1.wrapped_io', name='name_generator')],
 [FQN(module='example_1.wrapped_io', name='name_printer')],
 [FQN(module='example_1.wrapped_io', name='message')]]

```