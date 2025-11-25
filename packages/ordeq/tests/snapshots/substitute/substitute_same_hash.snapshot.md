## Resource

```python
from example_catalogs import local
from example_duplicates import duplicate_io_same_hash
from ordeq._substitute import _substitutes_modules_to_ios

print(_substitutes_modules_to_ios({duplicate_io_same_hash: local}))

```

## Output

```text
{MyIO(value='hello'): StringBuffer(_buffer=<_io.StringIO object at HASH1>), MyIO(value='result'): StringBuffer(_buffer=<_io.StringIO object at HASH2>)}

```