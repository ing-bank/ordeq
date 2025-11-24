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
  Node(func=example_resources.inline:generate, outputs=[CSV(path=Path('data1.csv'))])),
 (FQN(module='example_resources.inline', name='consume'),
  View(func=example_resources.inline:consume, inputs=[Text(path=Path('data1.csv'))])),
 (FQN(module='example_resources.pipeline', name='generate'),
  Node(func=example_resources.pipeline:generate, outputs=[CSV(path=Path('data2.csv'))])),
 (FQN(module='example_resources.pipeline', name='consume'),
  View(func=example_resources.pipeline:consume, inputs=[Text(path=Path('data2.csv'))])),
 (FQN(module='example_resources.updates', name='update'),
  Node(func=example_resources.updates:update, inputs=[CSV(path=Path('data3.csv'))], outputs=[CSV(path=Path('data3.csv'))])),
 (FQN(module='example_resources.updates', name='reflect'),
  Node(func=example_resources.updates:reflect, inputs=[CSV(path=Path('data3.csv'))], outputs=[Print()]))]
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