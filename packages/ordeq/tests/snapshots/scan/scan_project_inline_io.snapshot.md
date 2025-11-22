## Resource

```python
from pprint import pprint

import example_project.nodes_with_inline_io
from ordeq._scan import scan

nodes, ios = scan(example_project.nodes_with_inline_io)
print("Nodes:")
pprint(list(nodes.values()), width=200)
print("IOs:")
pprint(list(ios.values()), width=200)

```

## Output

```text
Nodes:
[('example_project.nodes_with_inline_io', 'greet')]
IOs:
[]

```