## Resource

```python
from pprint import pprint

import example_catalogs
from ordeq._resolve import _resolve_packages_to_modules
from ordeq._scan import scan

nodes, ios = scan(*_resolve_packages_to_modules(example_catalogs))
print("Nodes:")
pprint(list(nodes.values()), width=200)
print("IOs:")
pprint(list(ios.values()), width=200)

```

## Output

```text
Nodes:
[]
IOs:
[('example_catalogs.inconsistent', 'hello'),
 ('example_catalogs.local', 'hello'),
 ('example_catalogs.local', 'result'),
 ('example_catalogs.local_package', 'hello'),
 ('example_catalogs.local_package', 'result'),
 ('example_catalogs.package_base.creds', 'secret'),
 ('example_catalogs.package_base.etl', 'txs'),
 ('example_catalogs.package_base.etl', 'clients'),
 ('example_catalogs.package_base.ml', 'model'),
 ('example_catalogs.package_base.ml', 'predictions'),
 ('example_catalogs.package_base.ml', 'metrics'),
 ('example_catalogs.package_base.ml', 'plot'),
 ('example_catalogs.package_inconsistent.etl', 'txs'),
 ('example_catalogs.package_inconsistent.etl', 'clients'),
 ('example_catalogs.package_overlay.creds', 'secret'),
 ('example_catalogs.package_overlay.etl', 'clients'),
 ('example_catalogs.package_overlay.etl', 'txs'),
 ('example_catalogs.package_overlay.ml', 'model'),
 ('example_catalogs.package_overlay.ml', 'predictions'),
 ('example_catalogs.package_overlay.ml', 'metrics'),
 ('example_catalogs.package_overlay.ml', 'plot'),
 ('example_catalogs.remote_extended', 'hello'),
 ('example_catalogs.remote_overridden', 'result'),
 ('example_catalogs.remote_extended', 'another_io'),
 ('example_catalogs.remote_overridden', 'hello'),
 ('example_catalogs.remote_package', 'hello'),
 ('example_catalogs.remote_package', 'result')]

```