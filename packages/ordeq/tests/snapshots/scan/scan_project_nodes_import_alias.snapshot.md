## Resource

```python
from pprint import pprint

import example_project.nodes_import_alias
from ordeq._scan import scan

nodes, ios = scan(example_project.nodes_import_alias)
print("Nodes:")
pprint(list(nodes.values()), width=200)
print("IOs:")
pprint(list(ios.values()), width=200)

```

## Output

```text
Nodes:
[('example_project.nodes_import_alias', 'func')]
IOs:
[('example_project.nodes_import_alias', 'a'), ('example_project.nodes_import_alias', 'B'), ('example_project.nodes_import_alias', 'h')]

```