## Resource

```python
from pprint import pprint

import example_imports
from ordeq._scan import scan

nodes, ios = scan(example_imports)
print("Nodes:")
pprint(nodes)
print("IOs:")
pprint(ios)

```

## Output

```text
Nodes:
[]
IOs:
[(('example_imports.catalog', 'a'), IO(id=ID1))]

```