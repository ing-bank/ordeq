## Resource

```python
from pprint import pprint

import example_2
from ordeq._index import index

nodes, ios = index(example_2)
print("Nodes:")
pprint(nodes)
print("IOs:")
pprint(ios, width=40)

```

## Output

```text
Nodes:
{<function transform_input_2 at HASH1>: (('example_2.nodes',
                                                'transform_input_2'),
                                               <function transform_input_2 at HASH1>),
 Node(name=example_2.nodes:transform_input_2, inputs=[Input(id=ID1)], outputs=[Output(id=ID2)]): (('example_2.nodes',
                                                                                                                 'transform_input_2'),
                                                                                                                <function transform_input_2 at HASH1>),
 'example_2.nodes:transform_input_2': (('example_2.nodes', 'transform_input_2'),
                                       <function transform_input_2 at HASH1>),
 ('example_2.nodes', 'transform_input_2'): (('example_2.nodes',
                                             'transform_input_2'),
                                            <function transform_input_2 at HASH1>)}
IOs:
{4422777472: (('example_2.nodes',
               'TestInput2'),
              Input(id=ID1)),
 4422870160: (('example_2.nodes',
               'TestOutput2'),
              Output(id=ID2)),
 'example_2.catalog:TestInput2': (('example_2.catalog',
                                   'TestInput2'),
                                  Input(id=ID1)),
 'example_2.catalog:TestOutput2': (('example_2.catalog',
                                    'TestOutput2'),
                                   Output(id=ID2)),
 'example_2.nodes:TestInput2': (('example_2.nodes',
                                 'TestInput2'),
                                Input(id=ID1)),
 'example_2.nodes:TestOutput2': (('example_2.nodes',
                                  'TestOutput2'),
                                 Output(id=ID2)),
 ('example_2.catalog', 'TestInput2'): (('example_2.catalog',
                                        'TestInput2'),
                                       Input(id=ID1)),
 ('example_2.catalog', 'TestOutput2'): (('example_2.catalog',
                                         'TestOutput2'),
                                        Output(id=ID2)),
 ('example_2.nodes', 'TestInput2'): (('example_2.nodes',
                                      'TestInput2'),
                                     Input(id=ID1)),
 ('example_2.nodes', 'TestOutput2'): (('example_2.nodes',
                                       'TestOutput2'),
                                      Output(id=ID2))}

```