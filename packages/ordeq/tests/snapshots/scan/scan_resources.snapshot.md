## Resource

```python
from pprint import pprint

import example_resources
from ordeq._resolve import _resolve_packages_to_modules
from ordeq._scan import scan

nodes, ios = scan(*_resolve_packages_to_modules(example_resources))
print("Nodes:")
pprint(list(nodes.values()), width=200)
print("IOs:")
pprint(list(ios.values()), width=200)

```

## Output

```text
Nodes:
[('example_resources.inline', 'generate'),
 ('example_resources.inline', 'consume'),
 ('example_resources.pipeline', 'generate'),
 ('example_resources.pipeline', 'consume'),
 ('example_resources.updates', 'update'),
 ('example_resources.updates', 'reflect')]
IOs:
[('example_resources.pipeline', 'csv'),
 ('example_resources.pipeline', 'text'),
 ('example_resources.updates', 'csv'),
 ('example_resources.updates', 'csv_old'),
 ('example_resources.updates', 'csv_new')]

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