## Resource

```python
# Captures the behaviour when resolving a package catalog to IO.
from example_catalogs import package_base
from ordeq._resolve import _resolve_package_to_ios

ios = _resolve_package_to_ios(package_base)
print(ios)

```

## Output

```text
{('example_catalogs.package_base.creds', 'secret'): Literal('ohSoSecret!@#'), ('example_catalogs.package_base.etl', 'txs'): IO(idx=ID1), ('example_catalogs.package_base.etl', 'clients'): IO(idx=ID2), ('example_catalogs.package_base.ml', 'model'): IO(idx=ID3), ('example_catalogs.package_base.ml', 'predictions'): JSON(path=Path('predictions-base.json')), ('example_catalogs.package_base.ml', 'metrics'): IO(idx=ID4), ('example_catalogs.package_base.ml', 'plot'): IO(idx=ID5)}

```