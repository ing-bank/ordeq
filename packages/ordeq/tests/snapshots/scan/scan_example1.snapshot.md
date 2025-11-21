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
pprint(list(ios.values()), width=40)

```

## Output

```text
Nodes:
{<function transform_input at HASH1>: (('example_1.pipeline',
                                              'transform_input'),
                                             <function transform_input at HASH1>),
 <function world at HASH2>: (('example_1.nodes', 'world'),
                                   <function world at HASH2>),
 <function transform_mock_input at HASH3>: (('example_1.pipeline',
                                                   'transform_mock_input'),
                                                  <function transform_mock_input at HASH3>),
 <function hello at HASH4>: (('example_1.wrapped_io', 'hello'),
                                   <function hello at HASH4>),
 <function print_message at HASH5>: (('example_1.wrapped_io',
                                            'print_message'),
                                           <function print_message at HASH5>)}
IOs:
[(('example_1.pipeline', 'Hello'),
  StringBuffer(_buffer=<_io.StringIO object at HASH6>)),
 (('example_1.pipeline', 'World'),
  StringBuffer(_buffer=<_io.StringIO object at HASH7>)),
 (('example_1.pipeline', 'TestInput'),
  Input(id=ID1)),
 (('example_1.pipeline', 'TestOutput'),
  Output(id=ID2)),
 (('example_1.nodes', 'x'),
  StringBuffer(_buffer=<_io.StringIO object at HASH8>)),
 (('example_1.nodes', 'y'),
  StringBuffer(_buffer=<_io.StringIO object at HASH9>)),
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