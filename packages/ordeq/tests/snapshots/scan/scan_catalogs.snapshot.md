## Resource

```python
from pprint import pprint

import example_catalogs
from ordeq._scan import _scan_fqns

nodes, ios = _scan_fqns(example_catalogs)
print("Nodes:")
pprint(sorted(nodes, key=lambda n: (nodes[n], n.ref)), width=40)
print("IOs:")
pprint(list(ios.values()), width=40)

```

## Output

```text
Nodes:
[]
IOs:
[[FQN(module='example_catalogs.inconsistent', name='hello')],
 [FQN(module='example_catalogs.local', name='hello')],
 [FQN(module='example_catalogs.local', name='result')],
 [FQN(module='example_catalogs.local_package', name='hello')],
 [FQN(module='example_catalogs.local_package', name='result')],
 [FQN(module='example_catalogs.package_base.creds', name='secret')],
 [FQN(module='example_catalogs.package_base.etl', name='txs')],
 [FQN(module='example_catalogs.package_base.etl', name='clients')],
 [FQN(module='example_catalogs.package_base.ml', name='model')],
 [FQN(module='example_catalogs.package_base.ml', name='predictions')],
 [FQN(module='example_catalogs.package_base.ml', name='metrics')],
 [FQN(module='example_catalogs.package_base.ml', name='plot')],
 [FQN(module='example_catalogs.package_inconsistent.etl', name='txs')],
 [FQN(module='example_catalogs.package_inconsistent.etl', name='clients')],
 [FQN(module='example_catalogs.package_overlay.creds', name='secret')],
 [FQN(module='example_catalogs.package_overlay.etl', name='clients')],
 [FQN(module='example_catalogs.package_overlay.etl', name='txs')],
 [FQN(module='example_catalogs.package_overlay.ml', name='model')],
 [FQN(module='example_catalogs.package_overlay.ml', name='predictions')],
 [FQN(module='example_catalogs.package_overlay.ml', name='metrics')],
 [FQN(module='example_catalogs.package_overlay.ml', name='plot')],
 [FQN(module='example_catalogs.remote', name='hello'),
  FQN(module='example_catalogs.remote_extended', name='hello')],
 [FQN(module='example_catalogs.remote', name='result'),
  FQN(module='example_catalogs.remote_extended', name='result'),
  FQN(module='example_catalogs.remote_overridden', name='result')],
 [FQN(module='example_catalogs.remote_extended', name='another_io')],
 [FQN(module='example_catalogs.remote_overridden', name='hello')],
 [FQN(module='example_catalogs.remote_package', name='hello')],
 [FQN(module='example_catalogs.remote_package', name='result')]]

```