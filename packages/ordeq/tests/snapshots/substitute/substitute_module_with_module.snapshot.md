## Resource

```python
from example_catalogs import local, remote
from ordeq._substitute import _substitutes_modules_to_ios

# This is OK: 'local' and 'remote' both define the same entries
print(_substitutes_modules_to_ios({local: remote}))

```

## Output

```text
{StringBuffer(_buffer=<_io.StringIO object at HASH1>): StringBuffer(_buffer=<_io.StringIO object at HASH2>), StringBuffer(_buffer=<_io.StringIO object at HASH3>): StringBuffer(_buffer=<_io.StringIO object at HASH4>)}

```