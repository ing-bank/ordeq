## Resource

```python
# Captures the behaviour when resolving a package catalog to IO.
from example_catalogs import package_overlay
from ordeq._resolve import _resolve_module_to_ios

ios = _resolve_module_to_ios(package_overlay)
print(ios)

```

## Output

```text
{('example_catalogs.package_overlay.creds', 'secret'): Literal('ohSoSecret!@#'), ('example_catalogs.package_overlay.etl', 'txs'): IO(idx=ID1), ('example_catalogs.package_overlay.etl', 'clients'): StringBuffer(_buffer=<_io.StringIO object at HASH1>), ('example_catalogs.package_overlay.ml', 'model'): IO(idx=ID2), ('example_catalogs.package_overlay.ml', 'predictions'): JSON(path=Path('predictions-overlay.json')), ('example_catalogs.package_overlay.ml', 'metrics'): IO(idx=ID3), ('example_catalogs.package_overlay.ml', 'plot'): IO(idx=ID4)}

```