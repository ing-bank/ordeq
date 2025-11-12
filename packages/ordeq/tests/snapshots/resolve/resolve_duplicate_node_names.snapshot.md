## Resource

```python
# Captures the behaviour when resolving a module containing the same names
# for the same node.
from pprint import pprint

from example_duplicates import duplicate_node_names
from ordeq._resolve import _resolve_module_to_nodes

nodes = _resolve_module_to_nodes(duplicate_node_names)
pprint(nodes)

```

## Output

```text
[('example_duplicates.duplicate_node_names',
  'x',
  View(name=example_duplicates.duplicate_node_names:<lambda>))]

```