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
pprint(list(ios.values()), width=40)

```

## Output

```text
Nodes:
{<function consume at HASH1>: (('example_resources.inline', 'consume'),
                                     <function consume at HASH1>),
 <function generate at HASH2>: (('example_resources.inline', 'generate'),
                                      <function generate at HASH2>),
 <function consume at HASH3>: (('example_resources.pipeline', 'consume'),
                                     <function consume at HASH3>),
 <function generate at HASH4>: (('example_resources.pipeline',
                                       'generate'),
                                      <function generate at HASH4>),
 <function update at HASH5>: (('example_resources.updates', 'update'),
                                    <function update at HASH5>),
 <function reflect at HASH6>: (('example_resources.updates', 'reflect'),
                                     <function reflect at HASH6>)}
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