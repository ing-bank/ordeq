## Resource

```python
from pprint import pprint

import example_catalogs
from ordeq._scan import scan

nodes, ios = scan(example_catalogs)
print("Nodes:")
pprint(nodes)
print("IOs:")
pprint(ios)

```

## Output

```text
Nodes:
[]
IOs:
[[(('example_catalogs.inconsistent', 'hello'),
   StringBuffer(_buffer=<_io.StringIO object at HASH1>))],
 [(('example_catalogs.local', 'hello'),
   StringBuffer(_buffer=<_io.StringIO object at HASH2>))],
 [(('example_catalogs.local', 'result'),
   StringBuffer(_buffer=<_io.StringIO object at HASH3>))],
 [(('example_catalogs.local_package', 'hello'),
   StringBuffer(_buffer=<_io.StringIO object at HASH4>))],
 [(('example_catalogs.local_package', 'result'),
   StringBuffer(_buffer=<_io.StringIO object at HASH5>))],
 [(('example_catalogs.package_base.creds', 'secret'),
   Literal('ohSoSecret!@#'))],
 [(('example_catalogs.package_base.etl', 'txs'), IO(id=ID1))],
 [(('example_catalogs.package_base.etl', 'clients'), IO(id=ID2))],
 [(('example_catalogs.package_base.ml', 'model'), IO(id=ID3))],
 [(('example_catalogs.package_base.ml', 'predictions'),
   JSON(path=Path('predictions-base.json')))],
 [(('example_catalogs.package_base.ml', 'metrics'), IO(id=ID4))],
 [(('example_catalogs.package_base.ml', 'plot'), IO(id=ID5))],
 [(('example_catalogs.package_inconsistent.etl', 'txs'), IO(id=ID6))],
 [(('example_catalogs.package_inconsistent.etl', 'clients'),
   StringBuffer(_buffer=<_io.StringIO object at HASH6>))],
 [(('example_catalogs.package_overlay.creds', 'secret'),
   Literal('ohSoSecret!@#'))],
 [(('example_catalogs.package_overlay.etl', 'clients'),
   StringBuffer(_buffer=<_io.StringIO object at HASH7>))],
 [(('example_catalogs.package_overlay.etl', 'txs'), IO(id=ID7))],
 [(('example_catalogs.package_overlay.ml', 'model'), IO(id=ID8))],
 [(('example_catalogs.package_overlay.ml', 'predictions'),
   JSON(path=Path('predictions-overlay.json')))],
 [(('example_catalogs.package_overlay.ml', 'metrics'), IO(id=ID9))],
 [(('example_catalogs.package_overlay.ml', 'plot'), IO(id=ID10))],
 [(('example_catalogs.remote', 'hello'),
   StringBuffer(_buffer=<_io.StringIO object at HASH8>)),
  (('example_catalogs.remote_extended', 'hello'),
   StringBuffer(_buffer=<_io.StringIO object at HASH8>))],
 [(('example_catalogs.remote', 'result'),
   StringBuffer(_buffer=<_io.StringIO object at HASH9>)),
  (('example_catalogs.remote_extended', 'result'),
   StringBuffer(_buffer=<_io.StringIO object at HASH9>)),
  (('example_catalogs.remote_overridden', 'result'),
   StringBuffer(_buffer=<_io.StringIO object at HASH9>))],
 [(('example_catalogs.remote_extended', 'another_io'), Print())],
 [(('example_catalogs.remote_overridden', 'hello'),
   Literal('Hey I am overriding the hello IO'))],
 [(('example_catalogs.remote_package', 'hello'),
   StringBuffer(_buffer=<_io.StringIO object at HASH10>))],
 [(('example_catalogs.remote_package', 'result'),
   StringBuffer(_buffer=<_io.StringIO object at HASH11>))]]

```