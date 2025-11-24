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
[(FQN(module='example_resources.inline', name='generate'),
  Node(module=example_resources.inline, name=generate, outputs=[CSV(path=Path('data1.csv'))])),
 (FQN(module='example_resources.inline', name='consume'),
  View(module=example_resources.inline, name=consume, inputs=[Text(path=Path('data1.csv'))])),
 (FQN(module='example_resources.pipeline', name='generate'),
  Node(module=example_resources.pipeline, name=generate, outputs=[CSV(path=Path('data2.csv'))])),
 (FQN(module='example_resources.pipeline', name='consume'),
  View(module=example_resources.pipeline, name=consume, inputs=[Text(path=Path('data2.csv'))])),
 (FQN(module='example_resources.updates', name='update'),
  Node(module=example_resources.updates, name=update, inputs=[CSV(path=Path('data3.csv'))], outputs=[CSV(path=Path('data3.csv'))])),
 (FQN(module='example_resources.updates', name='reflect'),
  Node(module=example_resources.updates, name=reflect, inputs=[CSV(path=Path('data3.csv'))], outputs=[Print()]))]
IOs:
[(FQN(module='example_resources.pipeline', name='csv'),
  CSV(path=Path('data2.csv'))),
 (FQN(module='example_resources.pipeline', name='text'),
  Text(path=Path('data2.csv'))),
 (FQN(module='example_resources.updates', name='csv'),
  CSV(path=Path('data3.csv'))),
 (FQN(module='example_resources.updates', name='csv_old'),
  CSV(path=Path('data3.csv'))),
 (FQN(module='example_resources.updates', name='csv_new'),
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