## Resource

```python
from pprint import pprint

import example_project.nodes_import_alias
from ordeq._scan import scan

nodes, ios = scan(example_project.nodes_import_alias)
print("Nodes:")
pprint(nodes, width=200)
print("IOs:")
pprint(list(ios.values()), width=200)

```

## Output

```text
Nodes:
{<function func at HASH1>: ('example_project.nodes_import_alias', 'func')}
IOs:
[('example_project.nodes_import_alias', 'a'), ('example_project.nodes_import_alias', 'B'), ('example_project.nodes_import_alias', 'h')]

```