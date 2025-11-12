## Resource

```python
# Captures the behaviour when resolving a module containing the same names
# for the same node.
from pprint import pprint

from example_duplicates import duplicate_node_objects
from ordeq._resolve import _resolve_module_to_nodes

nodes = _resolve_module_to_nodes(duplicate_node_objects)
pprint(nodes)

```

## Output

```text
[('example_duplicates.duplicate_node_objects',
  'x',
  View(name=example_duplicates.duplicate_node_objects:<lambda>)),
 ('example_duplicates.duplicate_node_objects',
  'y',
  View(name=example_duplicates.duplicate_node_objects:<lambda>)),
 ('example_duplicates.duplicate_node_objects',
  'z',
  View(name=example_duplicates.duplicate_node_objects:<lambda>))]

```