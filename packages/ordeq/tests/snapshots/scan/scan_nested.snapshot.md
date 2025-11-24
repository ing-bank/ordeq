## Resource

```python
from pprint import pprint

import example_nested
from ordeq._scan import _scan_fqns

nodes, ios = _scan_fqns(example_nested)
print("Nodes:")
pprint(sorted(nodes, key=lambda n: n.ref), width=40)
print("IOs:")
pprint(list(ios.values()), width=40)

```

## Output

```text
Nodes:
[View(func=example_nested.subpackage.subsubpackage.hello:world),
 Node(module=example_nested.subpackage.subsubpackage.hello_relative, name=world_relative, outputs=[StringBuffer(_buffer=<_io.StringIO object at HASH1>)])]
IOs:
[[FQN(module='example_nested.catalog', name='message'),
  FQN(module='example_nested.subpackage.subsubpackage.hello_relative', name='message')]]

```