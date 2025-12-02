## Resource

```python
from pprint import pp

import example_resources
from ordeq._resolve import _resolve_packages_to_modules
from ordeq._scan import _scan_fqns

nodes, ios = _scan_fqns(*_resolve_packages_to_modules(example_resources))
print("Nodes:")
pp(nodes, width=40)
print("IOs:")
pp(list(ios.values()), width=40)

```

## Output

```text
Nodes:
{Node(module=example_resources.inline, name=generate, outputs=[CSV(path=Path('data1.csv'))]): [FQN(module='example_resources.inline', name='generate')],
 View(module=example_resources.inline, name=consume, inputs=[Text(path=Path('data1.csv'))]): [FQN(module='example_resources.inline', name='consume')],
 Node(module=example_resources.pipeline, name=generate, outputs=[CSV(path=Path('data2.csv'))]): [FQN(module='example_resources.pipeline', name='generate')],
 View(module=example_resources.pipeline, name=consume, inputs=[Text(path=Path('data2.csv'))]): [FQN(module='example_resources.pipeline', name='consume')],
 Node(module=example_resources.updates, name=update, inputs=[CSV(path=Path('data3.csv'))], outputs=[CSV(path=Path('data3.csv'))]): [FQN(module='example_resources.updates', name='update')],
 Node(module=example_resources.updates, name=reflect, inputs=[CSV(path=Path('data3.csv'))], outputs=[Print()]): [FQN(module='example_resources.updates', name='reflect')]}
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