## Resource

```python
from pprint import pprint

import example_references
from ordeq._index import index

nodes, ios = index(example_references)
print("Nodes:")
pprint(nodes)
print("IOs:")
pprint(ios, width=40)

```

## Output

```text
Nodes:
{}
IOs:
{4422515408: (('example_references.io_references',
               'named_nested_test_io'),
              Input(id=ID1)),
 4422777776: (('example_references.io_references',
               'named_test_io'),
              Input(id=ID2)),
 4424045568: (('example_references.io_references',
               'test_io'),
              Input(id=ID3)),
 4424110544: (('example_references.io_references',
               'nested_test_io'),
              Input(id=ID4)),
 4424273264: (('example_references.io_references',
               'world'),
              Literal('World!')),
 'example_references.io_references:named_nested_test_io': (('example_references.io_references',
                                                            'named_nested_test_io'),
                                                           Input(id=ID1)),
 'example_references.io_references:named_test_io': (('example_references.io_references',
                                                     'named_test_io'),
                                                    Input(id=ID2)),
 'example_references.io_references:nested_test_io': (('example_references.io_references',
                                                      'nested_test_io'),
                                                     Input(id=ID4)),
 'example_references.io_references:test_io': (('example_references.io_references',
                                               'test_io'),
                                              Input(id=ID3)),
 'example_references.io_references:world': (('example_references.io_references',
                                             'world'),
                                            Literal('World!')),
 ('example_references.io_references', 'named_nested_test_io'): (('example_references.io_references',
                                                                 'named_nested_test_io'),
                                                                Input(id=ID1)),
 ('example_references.io_references', 'named_test_io'): (('example_references.io_references',
                                                          'named_test_io'),
                                                         Input(id=ID2)),
 ('example_references.io_references', 'nested_test_io'): (('example_references.io_references',
                                                           'nested_test_io'),
                                                          Input(id=ID4)),
 ('example_references.io_references', 'test_io'): (('example_references.io_references',
                                                    'test_io'),
                                                   Input(id=ID3)),
 ('example_references.io_references', 'world'): (('example_references.io_references',
                                                  'world'),
                                                 Literal('World!'))}

```