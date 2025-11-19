## Resource

```python
from pprint import pprint

import example_project.nodes_with_inline_io
from ordeq._scan import scan

nodes, ios = scan(example_project.nodes_with_inline_io)
print("Nodes:")
pprint(list(nodes.items()))
print("IOs:")
pprint(list(ios.values()))

```

## Output

```text
Nodes:
[(Node(name=example_project.nodes_with_inline_io:greet, inputs=[Literal('Buenos dias')], outputs=[IO(id=ID1)]),
  [('example_project.nodes_with_inline_io', 'greet')])]
IOs:
[]

```