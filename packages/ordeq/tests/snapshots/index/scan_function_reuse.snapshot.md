## Resource

```python
from pprint import pprint

import example_function_reuse
from ordeq._index import index

nodes, ios = index(example_function_reuse)
print("Nodes:")
pprint(nodes)
print("IOs:")
pprint(list(ios.values()), width=40)

```

## Output

```text
Nodes:
{<function print_input at HASH1>: (('example_function_reuse.nodes', 'a'),
                                         <function print_input at HASH1>),
 <function print_input at HASH2>: (('example_function_reuse.nodes', 'b'),
                                         <function print_input at HASH2>),
 <function print_input at HASH3>: (('example_function_reuse.nodes', 'c'),
                                         <function print_input at HASH3>),
 <function print_input at HASH4>: (('example_function_reuse.nodes', 'd'),
                                         <function print_input at HASH4>),
 <function pi at HASH5>: (('example_function_reuse.nodes', 'pi'),
                                <function pi at HASH5>),
 View(name=example_function_reuse.func_defs:print_input, inputs=[StringBuffer(_buffer=<_io.StringIO object at HASH6>)]): (('example_function_reuse.nodes',
                                                                                                                                 'b'),
                                                                                                                                <function print_input at HASH2>),
 View(name=example_function_reuse.func_defs:print_input, inputs=[StringBuffer(_buffer=<_io.StringIO object at HASH7>)]): (('example_function_reuse.nodes',
                                                                                                                                 'a'),
                                                                                                                                <function print_input at HASH1>),
 View(name=example_function_reuse.func_defs:print_input, inputs=[StringBuffer(_buffer=<_io.StringIO object at HASH8>)]): (('example_function_reuse.nodes',
                                                                                                                                 'c'),
                                                                                                                                <function print_input at HASH3>),
 View(name=example_function_reuse.func_defs:print_input, inputs=[StringBuffer(_buffer=<_io.StringIO object at HASH9>)]): (('example_function_reuse.nodes',
                                                                                                                                 'd'),
                                                                                                                                <function print_input at HASH4>),
 View(name=example_function_reuse.nodes:pi, inputs=[StringBuffer(_buffer=<_io.StringIO object at HASH7>)]): (('example_function_reuse.nodes',
                                                                                                                    'pi'),
                                                                                                                   <function pi at HASH5>),
 'example_function_reuse.nodes:a': (('example_function_reuse.nodes', 'a'),
                                    <function print_input at HASH1>),
 'example_function_reuse.nodes:b': (('example_function_reuse.nodes', 'b'),
                                    <function print_input at HASH2>),
 'example_function_reuse.nodes:c': (('example_function_reuse.nodes', 'c'),
                                    <function print_input at HASH3>),
 'example_function_reuse.nodes:d': (('example_function_reuse.nodes', 'd'),
                                    <function print_input at HASH4>),
 'example_function_reuse.nodes:pi': (('example_function_reuse.nodes', 'pi'),
                                     <function pi at HASH5>),
 ('example_function_reuse.nodes', 'a'): (('example_function_reuse.nodes', 'a'),
                                         <function print_input at HASH1>),
 ('example_function_reuse.nodes', 'b'): (('example_function_reuse.nodes', 'b'),
                                         <function print_input at HASH2>),
 ('example_function_reuse.nodes', 'c'): (('example_function_reuse.nodes', 'c'),
                                         <function print_input at HASH3>),
 ('example_function_reuse.nodes', 'd'): (('example_function_reuse.nodes', 'd'),
                                         <function print_input at HASH4>),
 ('example_function_reuse.nodes', 'pi'): (('example_function_reuse.nodes',
                                           'pi'),
                                          <function pi at HASH5>)}
IOs:
[(('example_function_reuse.nodes', 'A'),
  StringBuffer(_buffer=<_io.StringIO object at HASH7>)),
 (('example_function_reuse.catalog',
   'A'),
  StringBuffer(_buffer=<_io.StringIO object at HASH7>)),
 (('example_function_reuse.catalog',
   'A'),
  StringBuffer(_buffer=<_io.StringIO object at HASH7>)),
 (('example_function_reuse.nodes', 'B'),
  StringBuffer(_buffer=<_io.StringIO object at HASH6>)),
 (('example_function_reuse.catalog',
   'B'),
  StringBuffer(_buffer=<_io.StringIO object at HASH6>)),
 (('example_function_reuse.catalog',
   'B'),
  StringBuffer(_buffer=<_io.StringIO object at HASH6>)),
 (('example_function_reuse.catalog',
   'C'),
  StringBuffer(_buffer=<_io.StringIO object at HASH8>)),
 (('example_function_reuse.catalog',
   'C'),
  StringBuffer(_buffer=<_io.StringIO object at HASH8>)),
 (('example_function_reuse.catalog',
   'C'),
  StringBuffer(_buffer=<_io.StringIO object at HASH8>)),
 (('example_function_reuse.catalog',
   'D'),
  StringBuffer(_buffer=<_io.StringIO object at HASH9>)),
 (('example_function_reuse.catalog',
   'D'),
  StringBuffer(_buffer=<_io.StringIO object at HASH9>)),
 (('example_function_reuse.catalog',
   'D'),
  StringBuffer(_buffer=<_io.StringIO object at HASH9>)),
 (('example_function_reuse.nodes', 'A'),
  StringBuffer(_buffer=<_io.StringIO object at HASH7>)),
 (('example_function_reuse.nodes', 'A'),
  StringBuffer(_buffer=<_io.StringIO object at HASH7>)),
 (('example_function_reuse.nodes', 'B'),
  StringBuffer(_buffer=<_io.StringIO object at HASH6>)),
 (('example_function_reuse.nodes', 'B'),
  StringBuffer(_buffer=<_io.StringIO object at HASH6>))]

```