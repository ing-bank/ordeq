## Resource

```python
# Captures the behaviour when resolving a package catalog to IO.
from pprint import pprint

from example_catalogs import package_overlay
from ordeq._resolve import _resolve_package_to_ios

ios = _resolve_package_to_ios(package_overlay)
pprint(ios)

```

## Output

```text
{'example_catalogs.package_overlay.creds': {'secret': Literal('ohSoSecret!@#')},
 'example_catalogs.package_overlay.etl': {'clients': StringBuffer(_buffer=<_io.StringIO object at HASH1>),
                                          'txs': IO(id=ID1)},
 'example_catalogs.package_overlay.ml': {'metrics': IO(id=ID2),
                                         'model': IO(id=ID3),
                                         'plot': IO(id=ID4),
                                         'predictions': JSON(path=Path('predictions-overlay.json'))}}

```