## Resource

```python
from pprint import pprint

import example_references
from ordeq._scan import scan

nodes, ios = scan(example_references)
print("Nodes:")
pprint(list(nodes.items()))
print("IOs:")
pprint(list(ios.values()))

```

## Output

```text
Nodes:
[]
IOs:
[[(('example_references.io_references', 'test_io'), Input(id=ID1))],
 [(('example_references.io_references', 'nested_test_io'),
   Input(id=ID2))],
 [(('example_references.io_references', 'world'), Literal('World!'))],
 [(('example_references.io_references', 'named_test_io'),
   Input(id=ID3))],
 [(('example_references.io_references', 'named_nested_test_io'),
   Input(id=ID4))]]

```