## Resource

```python
from pprint import pprint

import example_resources
from ordeq._resolve import _resolve_packages_to_modules
from ordeq._scan import scan

nodes, ios = scan(*_resolve_packages_to_modules(example_resources))
print("Nodes:")
pprint(nodes, width=200)
print("IOs:")
pprint(list(ios.values()), width=200)

```

## Output

```text
Nodes:
{<function reflect at HASH1>: ('example_resources.updates', 'reflect'),
 <function generate at HASH2>: ('example_resources.pipeline', 'generate'),
 <function generate at HASH3>: ('example_resources.inline', 'generate'),
 <function update at HASH4>: ('example_resources.updates', 'update'),
 <function consume at HASH5>: ('example_resources.pipeline', 'consume'),
 <function consume at HASH6>: ('example_resources.inline', 'consume')}
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