## Resource

```python
from pprint import pprint

import example_empty
from ordeq._scan import scan

nodes, ios = scan(example_empty)
print("Nodes:")
pprint(list(nodes.items()))
print("IOs:")
pprint(list(ios.values()))

```

## Output

```text
Nodes:
[]
IOs:
[]

```