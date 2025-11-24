## Resource

```python
from pprint import pprint

import example_catalogs
from ordeq._resolve import _resolve_packages_to_modules
from ordeq._scan import scan

nodes, ios = scan(*_resolve_packages_to_modules(example_catalogs))
print("Nodes:")
pprint(nodes)
print("IOs:")
pprint(ios, width=40)

```

## Output

```text
Nodes:
[]
IOs:
[(FQN(module='example_catalogs.inconsistent', name='hello'),
  StringBuffer(_buffer=<_io.StringIO object at HASH1>)),
 (FQN(module='example_catalogs.local', name='hello'),
  StringBuffer(_buffer=<_io.StringIO object at HASH2>)),
 (FQN(module='example_catalogs.local', name='result'),
  StringBuffer(_buffer=<_io.StringIO object at HASH3>)),
 (FQN(module='example_catalogs.local_package', name='hello'),
  StringBuffer(_buffer=<_io.StringIO object at HASH4>)),
 (FQN(module='example_catalogs.local_package', name='result'),
  StringBuffer(_buffer=<_io.StringIO object at HASH5>)),
 (FQN(module='example_catalogs.package_base.creds', name='secret'),
  Literal('ohSoSecret!@#')),
 (FQN(module='example_catalogs.package_base.etl', name='txs'),
  IO(id=ID1)),
 (FQN(module='example_catalogs.package_base.etl', name='clients'),
  IO(id=ID2)),
 (FQN(module='example_catalogs.package_base.ml', name='model'),
  IO(id=ID3)),
 (FQN(module='example_catalogs.package_base.ml', name='predictions'),
  JSON(path=Path('predictions-base.json'))),
 (FQN(module='example_catalogs.package_base.ml', name='metrics'),
  IO(id=ID4)),
 (FQN(module='example_catalogs.package_base.ml', name='plot'),
  IO(id=ID5)),
 (FQN(module='example_catalogs.package_inconsistent.etl', name='txs'),
  IO(id=ID6)),
 (FQN(module='example_catalogs.package_inconsistent.etl', name='clients'),
  StringBuffer(_buffer=<_io.StringIO object at HASH6>)),
 (FQN(module='example_catalogs.package_overlay.creds', name='secret'),
  Literal('ohSoSecret!@#')),
 (FQN(module='example_catalogs.package_overlay.etl', name='clients'),
  StringBuffer(_buffer=<_io.StringIO object at HASH7>)),
 (FQN(module='example_catalogs.package_overlay.etl', name='txs'),
  IO(id=ID7)),
 (FQN(module='example_catalogs.package_overlay.ml', name='model'),
  IO(id=ID8)),
 (FQN(module='example_catalogs.package_overlay.ml', name='predictions'),
  JSON(path=Path('predictions-overlay.json'))),
 (FQN(module='example_catalogs.package_overlay.ml', name='metrics'),
  IO(id=ID9)),
 (FQN(module='example_catalogs.package_overlay.ml', name='plot'),
  IO(id=ID10)),
 (FQN(module='example_catalogs.remote', name='hello'),
  StringBuffer(_buffer=<_io.StringIO object at HASH8>)),
 (FQN(module='example_catalogs.remote_extended', name='hello'),
  StringBuffer(_buffer=<_io.StringIO object at HASH8>)),
 (FQN(module='example_catalogs.remote', name='result'),
  StringBuffer(_buffer=<_io.StringIO object at HASH9>)),
 (FQN(module='example_catalogs.remote_extended', name='result'),
  StringBuffer(_buffer=<_io.StringIO object at HASH9>)),
 (FQN(module='example_catalogs.remote_overridden', name='result'),
  StringBuffer(_buffer=<_io.StringIO object at HASH9>)),
 (FQN(module='example_catalogs.remote_extended', name='another_io'),
  Print()),
 (FQN(module='example_catalogs.remote_overridden', name='hello'),
  Literal('Hey I am overriding the hello IO')),
 (FQN(module='example_catalogs.remote_package', name='hello'),
  StringBuffer(_buffer=<_io.StringIO object at HASH10>)),
 (FQN(module='example_catalogs.remote_package', name='result'),
  StringBuffer(_buffer=<_io.StringIO object at HASH11>))]

```