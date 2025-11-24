## Resource

```python
from pprint import pprint

import example_project.nodes_with_inline_io
from ordeq._scan import scan

nodes, ios = scan(example_project.nodes_with_inline_io)
print("Nodes:")
pprint(nodes)
print("IOs:")
pprint(ios, width=40)

```

## Output

```text
Nodes:
[(FQN(module='example_project.nodes_with_inline_io', name='greet'),
  Node(module=example_project.nodes_with_inline_io, name=greet, inputs=[Input(id=ID1)], outputs=[IO(id=ID2)]))]
IOs:
[]

```