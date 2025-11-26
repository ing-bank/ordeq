## Resource

```python
from pprint import pp

import example_project.nodes_with_inline_io
from ordeq._scan import _scan_fqns

nodes, ios = _scan_fqns(example_project.nodes_with_inline_io)
print("Nodes:")
pp(nodes, width=40)
print("IOs:")
pp(list(ios.values()), width=40)

```

## Output

```text
Nodes:
{Node(module=example_project.nodes_with_inline_io, name=greet, inputs=[Input(id=ID1)], outputs=[IO(id=ID2)]): [FQN(module='example_project.nodes_with_inline_io', name='greet')]}
IOs:
[]

```