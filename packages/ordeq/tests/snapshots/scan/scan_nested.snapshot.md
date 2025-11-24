## Resource

```python
from pprint import pp

import example_nested
from ordeq._scan import _scan_fqns

nodes, ios = _scan_fqns(example_nested)
print("Nodes:")
pp(nodes, width=40)
print("IOs:")
pp(list(ios.values()), width=40)

```

## Output

```text
Nodes:
{Node(module=example_nested.subpackage.subsubpackage.hello_relative, name=world_relative, outputs=[StringBuffer(_buffer=<_io.StringIO object at HASH1>)]): [FQN(module='example_nested.__main__', name='world_relative'),
                                                                                                                                                                  FQN(module='example_nested.subpackage.subsubpackage.hello_relative', name='world_relative')],
 View(func=example_nested.subpackage.subsubpackage.hello:world): [FQN(module='example_nested.subpackage.subsubpackage.hello', name='world')]}
IOs:
[[FQN(module='example_nested.catalog', name='message'),
  FQN(module='example_nested.subpackage.subsubpackage.hello_relative', name='message')]]

```