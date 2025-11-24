## Resource

```python
from example_catalogs import local, package_base, package_overlay, remote
from ordeq._substitute import _substitutes_modules_to_ios

# Should return entries for all IOs in the modules and packages:
print(
    _substitutes_modules_to_ios({local: remote, package_base: package_overlay})
)

```

## Output

```text
{StringBuffer(_buffer=<_io.StringIO object at HASH1>): StringBuffer(_buffer=<_io.StringIO object at HASH2>), StringBuffer(_buffer=<_io.StringIO object at HASH3>): StringBuffer(_buffer=<_io.StringIO object at HASH4>), Input(id=ID1): Input(id=ID2), IO(id=ID3): IO(id=ID4), IO(id=ID5): StringBuffer(_buffer=<_io.StringIO object at HASH5>), IO(id=ID6): IO(id=ID7), JSON(path=Path('predictions-base.json')): JSON(path=Path('predictions-overlay.json')), IO(id=ID8): IO(id=ID9), IO(id=ID10): IO(id=ID11)}

```