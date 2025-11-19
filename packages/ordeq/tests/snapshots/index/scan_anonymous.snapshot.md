## Resource

```python
from pprint import pprint

import example_anonymous
from ordeq._index import index

nodes, ios = index(example_anonymous)
print("Nodes:")
pprint(nodes)
print("IOs:")
pprint(ios, width=40)

```

## Output

```text
Nodes:
{<function node_with_inline_io at HASH1>: (('example_anonymous.nodes',
                                                  'node_with_inline_io'),
                                                 <function node_with_inline_io at HASH1>),
 Node(name=example_anonymous.nodes:node_with_inline_io, inputs=[IO(id=ID1)], outputs=[IO(id=ID2)]): (('example_anonymous.nodes',
                                                                                                                    'node_with_inline_io'),
                                                                                                                   <function node_with_inline_io at HASH1>),
 'example_anonymous.nodes:node_with_inline_io': (('example_anonymous.nodes',
                                                  'node_with_inline_io'),
                                                 <function node_with_inline_io at HASH1>),
 ('example_anonymous.nodes', 'node_with_inline_io'): (('example_anonymous.nodes',
                                                       'node_with_inline_io'),
                                                      <function node_with_inline_io at HASH1>)}
IOs:
{}

```