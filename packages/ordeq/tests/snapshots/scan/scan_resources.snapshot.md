## Resource

```python
from pprint import pprint

import example_resources
from ordeq._scan import _scan_fqns

nodes, ios = _scan_fqns(example_resources)
print("Nodes:")
pprint(sorted(nodes, key=lambda n: n.ref), width=40)
print("IOs:")
pprint(list(ios.values()), width=40)

```

## Output

```text
Nodes:
[View(module=example_resources.inline, name=consume, inputs=[Text(path=Path('data1.csv'))]),
 Node(module=example_resources.inline, name=generate, outputs=[CSV(path=Path('data1.csv'))]),
 View(module=example_resources.pipeline, name=consume, inputs=[Text(path=Path('data2.csv'))]),
 Node(module=example_resources.pipeline, name=generate, outputs=[CSV(path=Path('data2.csv'))]),
 Node(module=example_resources.updates, name=reflect, inputs=[CSV(path=Path('data3.csv'))], outputs=[Print()]),
 Node(module=example_resources.updates, name=update, inputs=[CSV(path=Path('data3.csv'))], outputs=[CSV(path=Path('data3.csv'))])]
IOs:
[[FQN(module='example_resources.pipeline', name='csv')],
 [FQN(module='example_resources.pipeline', name='text')],
 [FQN(module='example_resources.updates', name='csv')],
 [FQN(module='example_resources.updates', name='csv_old')],
 [FQN(module='example_resources.updates', name='csv_new')]]

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