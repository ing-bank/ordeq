## Resource

```python
from example_catalogs import local, package_base, package_overlay, remote
from ordeq._substitute import _substitutes_modules_to_ios

print(_substitutes_modules_to_ios({local: remote, package_base: package_overlay}))

```

## Output

```text
{StringBuffer(_buffer=<_io.StringIO object at HASH1>): StringBuffer(_buffer=<_io.StringIO object at HASH2>), StringBuffer(_buffer=<_io.StringIO object at HASH3>): StringBuffer(_buffer=<_io.StringIO object at HASH4>), Literal('ohSoSecret!@#'): Literal('ohSoSecret!@#'), IO(idx=ID1): IO(idx=ID2), IO(idx=ID3): StringBuffer(_buffer=<_io.StringIO object at HASH5>), IO(idx=ID4): IO(idx=ID5), JSON(path=Path('predictions-base.json')): JSON(path=Path('predictions-overlay.json')), IO(idx=ID6): IO(idx=ID7), IO(idx=ID8): IO(idx=ID9)}

```