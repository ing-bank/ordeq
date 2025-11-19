## Resource

```python
from pprint import pprint

import example_project.nodes_import
from ordeq._index import index

nodes, ios = index(example_project.nodes_import)
print("Nodes:")
pprint(nodes)
print("IOs:")
pprint(ios, width=40)

```

## Output

```text
Nodes:
{<function func_a at HASH1>: (('example_project.nodes_import', 'func_a'),
                                    <function func_a at HASH1>),
 <function func_b at HASH2>: (('example_project.nodes_import', 'func_b'),
                                    <function func_b at HASH2>),
 Node(name=example_project.nodes_import:func_a, inputs=[Literal('a'), StringBuffer(_buffer=<_io.StringIO object at HASH3>)], outputs=[Print()]): (('example_project.nodes_import',
                                                                                                                                                         'func_a'),
                                                                                                                                                        <function func_a at HASH1>),
 Node(name=example_project.nodes_import:func_b, inputs=[Literal('a'), StringBuffer(_buffer=<_io.StringIO object at HASH3>)], outputs=[Print()], attributes={'tags': {'viz': 'orange'}}): (('example_project.nodes_import',
                                                                                                                                                                                                 'func_b'),
                                                                                                                                                                                                <function func_b at HASH2>),
 'example_project.nodes_import:func_a': (('example_project.nodes_import',
                                          'func_a'),
                                         <function func_a at HASH1>),
 'example_project.nodes_import:func_b': (('example_project.nodes_import',
                                          'func_b'),
                                         <function func_b at HASH2>),
 ('example_project.nodes_import', 'func_a'): (('example_project.nodes_import',
                                               'func_a'),
                                              <function func_a at HASH1>),
 ('example_project.nodes_import', 'func_b'): (('example_project.nodes_import',
                                               'func_b'),
                                              <function func_b at HASH2>)}
IOs:
{4423730672: (('example_project.nodes_import',
               'a'),
              Literal('a')),
 4423737008: (('example_project.nodes_import',
               'f'),
              Print()),
 4424352144: (('example_project.nodes_import',
               'b'),
              StringBuffer(_buffer=<_io.StringIO object at HASH3>)),
 'example_project.nodes_import:a': (('example_project.nodes_import',
                                     'a'),
                                    Literal('a')),
 'example_project.nodes_import:b': (('example_project.nodes_import',
                                     'b'),
                                    StringBuffer(_buffer=<_io.StringIO object at HASH3>)),
 'example_project.nodes_import:f': (('example_project.nodes_import',
                                     'f'),
                                    Print()),
 ('example_project.nodes_import', 'a'): (('example_project.nodes_import',
                                          'a'),
                                         Literal('a')),
 ('example_project.nodes_import', 'b'): (('example_project.nodes_import',
                                          'b'),
                                         StringBuffer(_buffer=<_io.StringIO object at HASH3>)),
 ('example_project.nodes_import', 'f'): (('example_project.nodes_import',
                                          'f'),
                                         Print())}

```