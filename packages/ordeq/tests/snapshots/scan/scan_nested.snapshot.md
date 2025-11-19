## Resource

```python
from pprint import pprint

import example_nested
from ordeq._scan import scan

nodes, ios = scan(example_nested)
print("Nodes:")
pprint(list(nodes.items()))
print("IOs:")
pprint(list(ios.values()), width=40)

```

## Output

```text
Nodes:
[(View(name=example_nested.subpackage.subsubpackage.hello:world),
  [('example_nested.subpackage.subsubpackage.hello', 'world')])]
IOs:
[]

```