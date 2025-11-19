## Resource

```python
from pprint import pprint

import example_imports.aliased_catalog
from ordeq._scan import scan

nodes, ios = scan(example_imports.aliased_catalog)
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
[[(('example_imports.aliased_catalog', 'a'), IO(id=ID1))]]

```