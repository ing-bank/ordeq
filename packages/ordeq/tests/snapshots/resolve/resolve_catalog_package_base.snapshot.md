## Resource

```python
# Captures the behaviour when resolving a package catalog to IO.
from pprint import pprint

from example_catalogs import package_base
from ordeq._resolve import _resolve_package_to_ios

ios = _resolve_package_to_ios(package_base)
pprint(ios)

```

## Output

```text
{'example_catalogs.package_base.creds': {'secret': Literal('ohSoSecret!@#')},
 'example_catalogs.package_base.etl': {'clients': IO(id=ID1),
                                       'txs': IO(id=ID2)},
 'example_catalogs.package_base.ml': {'metrics': IO(id=ID3),
                                      'model': IO(id=ID4),
                                      'plot': IO(id=ID5),
                                      'predictions': JSON(path=Path('predictions-base.json'))}}

```