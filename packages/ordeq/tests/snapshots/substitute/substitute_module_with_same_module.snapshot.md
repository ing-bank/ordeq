## Resource

```python
from example_catalogs import local
from ordeq._substitute import _substitutes_modules_to_ios

# Should return an empty map
print(_substitutes_modules_to_ios({local: local}))

```

## Output

```text
{StringBuffer(_buffer=<_io.StringIO object at HASH1>): StringBuffer(_buffer=<_io.StringIO object at HASH1>), StringBuffer(_buffer=<_io.StringIO object at HASH2>): StringBuffer(_buffer=<_io.StringIO object at HASH2>)}

```