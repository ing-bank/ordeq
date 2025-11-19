## Resource

```python
from pprint import pprint

import example_2
from ordeq._scan import scan

nodes, ios = scan(example_2)
print("Nodes:")
pprint(nodes)
print("IOs:")
pprint(ios)

```

## Output

```text
Nodes:
[(('example_2.nodes', 'transform_input_2'),
  Node(name=example_2.nodes:transform_input_2, inputs=[Input(id=ID1)], outputs=[Output(id=ID2)]))]
IOs:
[[(('example_2.catalog', 'TestInput2'), Input(id=ID1)),
  (('example_2.nodes', 'TestInput2'), Input(id=ID1))],
 [(('example_2.catalog', 'TestOutput2'), Output(id=ID2)),
  (('example_2.nodes', 'TestOutput2'), Output(id=ID2))]]

```