## Resource

```python
from pprint import pprint

import example_project.nodes_with_inline_io
from ordeq._index import index

nodes, ios = index(example_project.nodes_with_inline_io)
print("Nodes:")
pprint(nodes)
print("IOs:")
pprint(ios, width=40)

```

## Output

```text
Nodes:
{<function greet at HASH1>: (('example_project.nodes_with_inline_io',
                                    'greet'),
                                   <function greet at HASH1>),
 Node(name=example_project.nodes_with_inline_io:greet, inputs=[Literal('Buenos dias')], outputs=[IO(id=ID1)]): (('example_project.nodes_with_inline_io',
                                                                                                                        'greet'),
                                                                                                                       <function greet at HASH1>),
 'example_project.nodes_with_inline_io:greet': (('example_project.nodes_with_inline_io',
                                                 'greet'),
                                                <function greet at HASH1>),
 ('example_project.nodes_with_inline_io', 'greet'): (('example_project.nodes_with_inline_io',
                                                      'greet'),
                                                     <function greet at HASH1>)}
IOs:
{}

```