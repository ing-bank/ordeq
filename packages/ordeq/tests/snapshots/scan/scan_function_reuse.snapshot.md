## Resource

```python
from pprint import pprint

import example_function_reuse
from ordeq._resolve import _resolve_packages_to_modules
from ordeq._scan import scan

nodes, ios = scan(*_resolve_packages_to_modules(example_function_reuse))
print("Nodes:")
pprint(nodes, width=200)
print("IOs:")
pprint(list(ios.values()), width=200)

```

## Output

```text
Nodes:
{<function print_input at HASH1>: ('example_function_reuse.nodes', 'a'),
 <function print_input at HASH2>: ('example_function_reuse.nodes', 'b'),
 <function print_input at HASH3>: ('example_function_reuse.nodes', 'c'),
 <function print_input at HASH4>: ('example_function_reuse.nodes', 'd'),
 <function pi at HASH5>: ('example_function_reuse.nodes', 'pi')}
IOs:
[('example_function_reuse.nodes', 'A'), ('example_function_reuse.nodes', 'B'), ('example_function_reuse.catalog', 'C'), ('example_function_reuse.catalog', 'D')]

```