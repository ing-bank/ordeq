## Resource

```python
from pprint import pprint

import example_project.nodes_with_inline_io
from ordeq._scan import scan

nodes, ios = scan(example_project.nodes_with_inline_io)
print("Nodes:")
pprint(nodes)
print("IOs:")
pprint(list(ios.values()), width=40)

```

## Output

```text
Nodes:
{<function greet at HASH1>: (('example_project.nodes_with_inline_io',
                                    'greet'),
                                   <function greet at HASH1>)}
IOs:
[]

```