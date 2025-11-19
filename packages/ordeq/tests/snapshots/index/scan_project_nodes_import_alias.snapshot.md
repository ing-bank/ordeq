## Resource

```python
from pprint import pprint

import example_project.nodes_import_alias
from ordeq._index import index

nodes, ios = index(example_project.nodes_import_alias)
print("Nodes:")
pprint(nodes)
print("IOs:")
pprint(ios, width=40)

```

## Output

```text
Nodes:
{<function func at HASH1>: (('example_project.nodes_import_alias',
                                   'func'),
                                  <function func at HASH1>),
 Node(name=example_project.nodes_import_alias:func, inputs=[Literal('a'), StringBuffer(_buffer=<_io.StringIO object at HASH2>)], outputs=[Print()], attributes={'tags': {'key': 'threshold', 'value': 0.23}}): (('example_project.nodes_import_alias',
                                                                                                                                                                                                                       'func'),
                                                                                                                                                                                                                      <function func at HASH1>),
 'example_project.nodes_import_alias:func': (('example_project.nodes_import_alias',
                                              'func'),
                                             <function func at HASH1>),
 ('example_project.nodes_import_alias', 'func'): (('example_project.nodes_import_alias',
                                                   'func'),
                                                  <function func at HASH1>)}
IOs:
{4423386800: (('example_project.nodes_import_alias',
               'h'),
              Print()),
 4423730672: (('example_project.nodes_import_alias',
               'a'),
              Literal('a')),
 4424352144: (('example_project.nodes_import_alias',
               'B'),
              StringBuffer(_buffer=<_io.StringIO object at HASH2>)),
 'example_project.nodes_import_alias:B': (('example_project.nodes_import_alias',
                                           'B'),
                                          StringBuffer(_buffer=<_io.StringIO object at HASH2>)),
 'example_project.nodes_import_alias:a': (('example_project.nodes_import_alias',
                                           'a'),
                                          Literal('a')),
 'example_project.nodes_import_alias:h': (('example_project.nodes_import_alias',
                                           'h'),
                                          Print()),
 ('example_project.nodes_import_alias', 'B'): (('example_project.nodes_import_alias',
                                                'B'),
                                               StringBuffer(_buffer=<_io.StringIO object at HASH2>)),
 ('example_project.nodes_import_alias', 'a'): (('example_project.nodes_import_alias',
                                                'a'),
                                               Literal('a')),
 ('example_project.nodes_import_alias', 'h'): (('example_project.nodes_import_alias',
                                                'h'),
                                               Print())}

```