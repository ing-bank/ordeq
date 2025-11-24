## Resource

```python
from pprint import pprint

import example_2
from ordeq._scan import _scan_fqns

nodes, ios = _scan_fqns(example_2)
print("Nodes:")
pprint(nodes, width=40)
print("IOs:")
pprint(list(ios.values()), width=40)

```

## Output

```text
Nodes:
{Node(module=example_2.nodes, name=transform_input_2, inputs=[Input(id=ID1)], outputs=[Output(id=ID2)]): [FQN(module='example_2.nodes', name='transform_input_2')]}
IOs:
[[FQN(module='example_2.catalog', name='TestInput2'),
  FQN(module='example_2.nodes', name='TestInput2')],
 [FQN(module='example_2.catalog', name='TestOutput2'),
  FQN(module='example_2.nodes', name='TestOutput2')]]

```