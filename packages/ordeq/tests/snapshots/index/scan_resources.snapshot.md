## Resource

```python
from pprint import pprint

import example_resources
from ordeq._index import index

nodes, ios = index(example_resources)
print("Nodes:")
pprint(nodes)
print("IOs:")
pprint(ios, width=40)

```

## Output

```text
Nodes:
{<function generate at HASH1>: (('example_resources.inline', 'generate'),
                                      <function generate at HASH1>),
 <function consume at HASH2>: (('example_resources.inline', 'consume'),
                                     <function consume at HASH2>),
 <function generate at HASH3>: (('example_resources.pipeline',
                                       'generate'),
                                      <function generate at HASH3>),
 <function consume at HASH4>: (('example_resources.pipeline', 'consume'),
                                     <function consume at HASH4>),
 <function update at HASH5>: (('example_resources.updates', 'update'),
                                    <function update at HASH5>),
 <function reflect at HASH6>: (('example_resources.updates', 'reflect'),
                                     <function reflect at HASH6>),
 Node(name=example_resources.inline:generate, outputs=[CSV(path=Path('data1.csv'))]): (('example_resources.inline',
                                                                                             'generate'),
                                                                                            <function generate at HASH1>),
 Node(name=example_resources.updates:reflect, inputs=[CSV(path=Path('data3.csv'))], outputs=[Print()]): (('example_resources.updates',
                                                                                                               'reflect'),
                                                                                                              <function reflect at HASH6>),
 Node(name=example_resources.updates:update, inputs=[CSV(path=Path('data3.csv'))], outputs=[CSV(path=Path('data3.csv'))]): (('example_resources.updates',
                                                                                                                                       'update'),
                                                                                                                                      <function update at HASH5>),
 Node(name=example_resources.pipeline:generate, outputs=[CSV(path=Path('data2.csv'))]): (('example_resources.pipeline',
                                                                                               'generate'),
                                                                                              <function generate at HASH3>),
 View(name=example_resources.inline:consume, inputs=[Text(path=Path('data1.csv'))]): (('example_resources.inline',
                                                                                            'consume'),
                                                                                           <function consume at HASH2>),
 View(name=example_resources.pipeline:consume, inputs=[Text(path=Path('data2.csv'))]): (('example_resources.pipeline',
                                                                                              'consume'),
                                                                                             <function consume at HASH4>),
 'example_resources.inline:consume': (('example_resources.inline', 'consume'),
                                      <function consume at HASH2>),
 'example_resources.inline:generate': (('example_resources.inline', 'generate'),
                                       <function generate at HASH1>),
 'example_resources.pipeline:consume': (('example_resources.pipeline',
                                         'consume'),
                                        <function consume at HASH4>),
 'example_resources.pipeline:generate': (('example_resources.pipeline',
                                          'generate'),
                                         <function generate at HASH3>),
 'example_resources.updates:reflect': (('example_resources.updates', 'reflect'),
                                       <function reflect at HASH6>),
 'example_resources.updates:update': (('example_resources.updates', 'update'),
                                      <function update at HASH5>),
 ('example_resources.inline', 'consume'): (('example_resources.inline',
                                            'consume'),
                                           <function consume at HASH2>),
 ('example_resources.inline', 'generate'): (('example_resources.inline',
                                             'generate'),
                                            <function generate at HASH1>),
 ('example_resources.pipeline', 'consume'): (('example_resources.pipeline',
                                              'consume'),
                                             <function consume at HASH4>),
 ('example_resources.pipeline', 'generate'): (('example_resources.pipeline',
                                               'generate'),
                                              <function generate at HASH3>),
 ('example_resources.updates', 'reflect'): (('example_resources.updates',
                                             'reflect'),
                                            <function reflect at HASH6>),
 ('example_resources.updates', 'update'): (('example_resources.updates',
                                            'update'),
                                           <function update at HASH5>)}
IOs:
{4423741328: (('example_resources.updates',
               'csv_old'),
              CSV(path=Path('data3.csv'))),
 4424178256: (('example_resources.pipeline',
               'text'),
              Text(path=Path('data2.csv'))),
 4424467728: (('example_resources.pipeline',
               'csv'),
              CSV(path=Path('data2.csv'))),
 4424470464: (('example_resources.updates',
               'csv'),
              CSV(path=Path('data3.csv'))),
 4424763056: (('example_resources.updates',
               'csv_new'),
              CSV(path=Path('data3.csv'))),
 'example_resources.pipeline:csv': (('example_resources.pipeline',
                                     'csv'),
                                    CSV(path=Path('data2.csv'))),
 'example_resources.pipeline:text': (('example_resources.pipeline',
                                      'text'),
                                     Text(path=Path('data2.csv'))),
 'example_resources.updates:csv': (('example_resources.updates',
                                    'csv'),
                                   CSV(path=Path('data3.csv'))),
 'example_resources.updates:csv_new': (('example_resources.updates',
                                        'csv_new'),
                                       CSV(path=Path('data3.csv'))),
 'example_resources.updates:csv_old': (('example_resources.updates',
                                        'csv_old'),
                                       CSV(path=Path('data3.csv'))),
 ('example_resources.pipeline', 'csv'): (('example_resources.pipeline',
                                          'csv'),
                                         CSV(path=Path('data2.csv'))),
 ('example_resources.pipeline', 'text'): (('example_resources.pipeline',
                                           'text'),
                                          Text(path=Path('data2.csv'))),
 ('example_resources.updates', 'csv'): (('example_resources.updates',
                                         'csv'),
                                        CSV(path=Path('data3.csv'))),
 ('example_resources.updates', 'csv_new'): (('example_resources.updates',
                                             'csv_new'),
                                            CSV(path=Path('data3.csv'))),
 ('example_resources.updates', 'csv_old'): (('example_resources.updates',
                                             'csv_old'),
                                            CSV(path=Path('data3.csv')))}

```

## Logging

```text
WARNING	ordeq.preview	Resources are in preview mode and may change without notice in future releases.
WARNING	ordeq.preview	Resources are in preview mode and may change without notice in future releases.
WARNING	ordeq.preview	Creating a view, as no outputs were provided for node 'example_resources.inline:consume'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.preview	Resources are in preview mode and may change without notice in future releases.
WARNING	ordeq.preview	Resources are in preview mode and may change without notice in future releases.
WARNING	ordeq.preview	Creating a view, as no outputs were provided for node 'example_resources.pipeline:consume'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.preview	Resources are in preview mode and may change without notice in future releases.
WARNING	ordeq.preview	Resources are in preview mode and may change without notice in future releases.

```