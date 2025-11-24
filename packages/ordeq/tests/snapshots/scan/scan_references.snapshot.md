## Resource

```python
from pprint import pp

import example_references
from ordeq._scan import _scan_fqns

nodes, ios = _scan_fqns(example_references)
print("Nodes:")
pp(nodes, width=40)
print("IOs:")
pp(list(ios.values()), width=40)

```

## Output

```text
Nodes:
{}
IOs:
[[FQN(module='example_references.io_references', name='test_io')],
 [FQN(module='example_references.io_references', name='nested_test_io')],
 [FQN(module='example_references.io_references', name='world')],
 [FQN(module='example_references.io_references', name='named_test_io')],
 [FQN(module='example_references.io_references', name='named_nested_test_io')]]

```