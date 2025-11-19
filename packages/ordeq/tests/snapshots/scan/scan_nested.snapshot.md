## Resource

```python
from pprint import pprint

import example_nested
from ordeq._scan import scan

nodes, ios = scan(example_nested)
print("Nodes:")
pprint(nodes)
print("IOs:")
pprint(ios, width=40)

```

## Output

```text
Nodes:
[(('example_nested.subpackage.subsubpackage.hello', 'world'),
  View(name=example_nested.subpackage.subsubpackage.hello:world))]
IOs:
[]

```