## Resource

```python
from pprint import pprint

import example_resources
from ordeq._resolve import _resolve_packages_to_modules
from ordeq._scan import scan

nodes, ios = scan(*_resolve_packages_to_modules(example_resources))
print("Nodes:")
pprint(nodes)
print("IOs:")
pprint(ios, width=40)

```

## Output

```text
Nodes:
[(('example_resources.inline', 'generate'),
  Node(module=example_resources.inline, name=generate, outputs=[CSV(path=Path('data1.csv'))])),
 (('example_resources.inline', 'consume'),
  View(module=example_resources.inline, name=consume, inputs=[Text(path=Path('data1.csv'))])),
 (('example_resources.pipeline', 'generate'),
  Node(module=example_resources.pipeline, name=generate, outputs=[CSV(path=Path('data2.csv'))])),
 (('example_resources.pipeline', 'consume'),
  View(module=example_resources.pipeline, name=consume, inputs=[Text(path=Path('data2.csv'))])),
 (('example_resources.updates', 'update'),
  Node(module=example_resources.updates, name=update, inputs=[CSV(path=Path('data3.csv'))], outputs=[CSV(path=Path('data3.csv'))])),
 (('example_resources.updates', 'reflect'),
  Node(module=example_resources.updates, name=reflect, inputs=[CSV(path=Path('data3.csv'))], outputs=[Print()]))]
IOs:
[(('example_resources.pipeline', 'csv'),
  CSV(path=Path('data2.csv'))),
 (('example_resources.pipeline',
   'text'),
  Text(path=Path('data2.csv'))),
 (('example_resources.updates', 'csv'),
  CSV(path=Path('data3.csv'))),
 (('example_resources.updates',
   'csv_old'),
  CSV(path=Path('data3.csv'))),
 (('example_resources.updates',
   'csv_new'),
  CSV(path=Path('data3.csv')))]

```

## Logging

```text
WARNING	ordeq.preview	Resources are in preview mode and may change without notice in future releases.
WARNING	ordeq.preview	Resources are in preview mode and may change without notice in future releases.
WARNING	ordeq.preview	Resources are in preview mode and may change without notice in future releases.
WARNING	ordeq.preview	Resources are in preview mode and may change without notice in future releases.
WARNING	ordeq.preview	Resources are in preview mode and may change without notice in future releases.
WARNING	ordeq.preview	Resources are in preview mode and may change without notice in future releases.

```