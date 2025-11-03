## Resource

```python
from ordeq._substitute import _build_substitution_map

from example_catalogs import local, remote

# This is OK: 'local' and 'remote' both define the same entries
print(_build_substitution_map({local: remote}))

```

## Output

```text
{StringBuffer(_buffer=<_io.StringIO object at HASH1>): StringBuffer(_buffer=<_io.StringIO object at HASH2>), StringBuffer(_buffer=<_io.StringIO object at HASH3>): StringBuffer(_buffer=<_io.StringIO object at HASH4>)}

```