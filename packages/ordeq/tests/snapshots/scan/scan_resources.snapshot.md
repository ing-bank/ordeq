## Resource

```python
from pprint import pprint

import example_resources
from ordeq._scan import scan

nodes, ios = scan(example_resources)
print("Nodes:")
pprint(list(nodes.items()))
print("IOs:")
pprint(list(ios.values()), width=40)

```

## Output

```text
Nodes:
[(Node(name=example_resources.inline:generate, outputs=[CSV(path=Path('data1.csv'))]),
  [('example_resources.inline', 'generate')]),
 (View(name=example_resources.inline:consume, inputs=[Text(path=Path('data1.csv'))]),
  [('example_resources.inline', 'consume')]),
 (Node(name=example_resources.pipeline:generate, outputs=[CSV(path=Path('data2.csv'))]),
  [('example_resources.pipeline', 'generate')]),
 (View(name=example_resources.pipeline:consume, inputs=[Text(path=Path('data2.csv'))]),
  [('example_resources.pipeline', 'consume')]),
 (Node(name=example_resources.updates:update, inputs=[CSV(path=Path('data3.csv'))], outputs=[CSV(path=Path('data3.csv'))]),
  [('example_resources.updates', 'update')]),
 (Node(name=example_resources.updates:reflect, inputs=[CSV(path=Path('data3.csv'))], outputs=[Print()]),
  [('example_resources.updates', 'reflect')])]
IOs:
[[(('example_resources.pipeline',
    'csv'),
   CSV(path=Path('data2.csv')))],
 [(('example_resources.pipeline',
    'text'),
   Text(path=Path('data2.csv')))],
 [(('example_resources.updates', 'csv'),
   CSV(path=Path('data3.csv')))],
 [(('example_resources.updates',
    'csv_old'),
   CSV(path=Path('data3.csv')))],
 [(('example_resources.updates',
    'csv_new'),
   CSV(path=Path('data3.csv')))]]

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