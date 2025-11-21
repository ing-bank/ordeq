## Resource

```python
from pprint import pprint

import example_function_reuse
from ordeq._resolve import _resolve_packages_to_modules
from ordeq._scan import scan

nodes, ios = scan(*_resolve_packages_to_modules(example_function_reuse))
print("Nodes:")
pprint(list(nodes.values()), width=200)
print("IOs:")
pprint(list(ios.values()), width=200)

```

## Output

```text
Nodes:
[('example_function_reuse.nodes', 'a'), ('example_function_reuse.nodes', 'b'), ('example_function_reuse.nodes', 'c'), ('example_function_reuse.nodes', 'd'), ('example_function_reuse.nodes', 'pi')]
IOs:
[('example_function_reuse.nodes', 'A'), ('example_function_reuse.nodes', 'B'), ('example_function_reuse.catalog', 'C'), ('example_function_reuse.catalog', 'D')]

```