## Resource

```python
from pprint import pprint

import example_project.nodes_import
from ordeq._scan import scan

nodes, ios = scan(example_project.nodes_import)
print("Nodes:")
pprint(nodes, width=200)
print("IOs:")
pprint(list(ios.values()), width=200)

```

## Output

```text
Nodes:
{<function func_b at HASH1>: ('example_project.nodes_import', 'func_b'), <function func_a at HASH2>: ('example_project.nodes_import', 'func_a')}
IOs:
[('example_project.nodes_import', 'a'), ('example_project.nodes_import', 'b'), ('example_project.nodes_import', 'f')]

```