## Resource

```python
from pprint import pp

import example_project
from ordeq._resolve import _resolve_packages_to_modules
from ordeq._scan import _scan_fqns

nodes, ios = _scan_fqns(*_resolve_packages_to_modules(example_project))
print("Nodes:")
pp(nodes, width=40)
print("IOs:")
pp(list(ios.values()), width=40)

```

## Output

```text
Nodes:
{Node(module=example_project.inner.nodes, name=func, inputs=[IO(id=ID1)], outputs=[Print()], attributes={'tags': ['dummy']}): [FQN(module='example_project.inner.nodes', name='func')],
 Node(module=example_project.nodes, name=func, inputs=[IO(id=ID2)], outputs=[Print()], attributes={'tags': ['dummy']}): [FQN(module='example_project.nodes', name='func')],
 Node(module=example_project.nodes_import, name=func_a, inputs=[Input(id=ID3), StringBuffer(_buffer=<_io.StringIO object at HASH1>)], outputs=[Print()]): [FQN(module='example_project.nodes_import', name='func_a')],
 Node(module=example_project.nodes_import, name=func_b, inputs=[Input(id=ID3), StringBuffer(_buffer=<_io.StringIO object at HASH1>)], outputs=[Print()], attributes={'tags': {'viz': 'orange'}}): [FQN(module='example_project.nodes_import', name='func_b')],
 Node(module=example_project.nodes_import_alias, name=func, inputs=[Input(id=ID3), StringBuffer(_buffer=<_io.StringIO object at HASH1>)], outputs=[Print()], attributes={'tags': {'key': 'threshold', 'value': 0.23}}): [FQN(module='example_project.nodes_import_alias', name='func')],
 Node(module=example_project.nodes_with_inline_io, name=greet, inputs=[Input(id=ID4)], outputs=[IO(id=ID5)]): [FQN(module='example_project.nodes_with_inline_io', name='greet')],
 View(module=example_project.nodes_with_view, name=greet, inputs=[Input(id=ID6)]): [FQN(module='example_project.nodes_with_view', name='greet')],
 Node(module=example_project.nodes_with_view, name=farewell, inputs=[IO(id=ID7)], outputs=[Print()]): [FQN(module='example_project.nodes_with_view', name='farewell')]}
IOs:
[[FQN(module='example_project.catalog_1', name='a'),
  FQN(module='example_project.nodes_import', name='a'),
  FQN(module='example_project.nodes_import_alias', name='a')],
 [FQN(module='example_project.catalog_1', name='b'),
  FQN(module='example_project.nodes_import', name='b'),
  FQN(module='example_project.nodes_import_alias', name='b')],
 [FQN(module='example_project.catalog_1', name='c')],
 [FQN(module='example_project.catalog_2', name='d')],
 [FQN(module='example_project.catalog_2', name='e')],
 [FQN(module='example_project.catalog_2', name='f'),
  FQN(module='example_project.nodes_import', name='f')],
 [FQN(module='example_project.catalog_2', name='g')],
 [FQN(module='example_project.catalog_2', name='h'),
  FQN(module='example_project.nodes_import_alias', name='h')],
 [FQN(module='example_project.catalog_2', name='i')],
 [FQN(module='example_project.catalog_2', name='j')],
 [FQN(module='example_project.inner.nodes', name='x')],
 [FQN(module='example_project.inner.nodes', name='y')],
 [FQN(module='example_project.nodes', name='x')],
 [FQN(module='example_project.nodes', name='y')],
 [FQN(module='example_project.nodes_with_view', name='greeting')],
 [FQN(module='example_project.nodes_with_view', name='printer')]]

```