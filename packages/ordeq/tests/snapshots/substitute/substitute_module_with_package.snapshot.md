## Resource

```python
from ordeq._substitute import _build_substitution_map

from example_catalogs import local, remote_package

# This is OK: though 'local' is a file-module and 'remote_package' is a
# package, they both define the same entries and are both of ModuleType.
print(_build_substitution_map({local: remote_package}))

```

## Output

```text
{StringBuffer(_buffer=<_io.StringIO object at HASH1>): StringBuffer(_buffer=<_io.StringIO object at HASH2>), StringBuffer(_buffer=<_io.StringIO object at HASH3>): StringBuffer(_buffer=<_io.StringIO object at HASH4>)}

```