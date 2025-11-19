## Resource

```python
from pprint import pprint

import example_empty
from ordeq._index import index

nodes, ios = index(example_empty)
print("Nodes:")
pprint(nodes)
print("IOs:")
pprint(list(ios.values()), width=40)

```

## Output

```text
Nodes:
{}
IOs:
[]

```