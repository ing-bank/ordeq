## Resource

```python
from pprint import pprint

import example_empty
from ordeq._scan import scan

nodes, ios = scan(example_empty)
print("Nodes:")
pprint(nodes)
print("IOs:")
pprint(ios, width=40)

```

## Output

```text
Nodes:
[]
IOs:
[]

```