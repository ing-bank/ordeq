## Resource

```python
from example_catalogs import local
from example_duplicates import duplicate_io_same_hash
from ordeq._substitute import _substitutes_modules_to_ios

print(_substitutes_modules_to_ios({duplicate_io_same_hash: local}))

print(_substitutes_modules_to_ios({local: duplicate_io_same_hash}))

```

## Output

```text
{MyIO(value='hello', attr=0): StringBuffer(_buffer=<_io.StringIO object at HASH1>), MyIO(value='result', attr=0): StringBuffer(_buffer=<_io.StringIO object at HASH2>)}
{StringBuffer(_buffer=<_io.StringIO object at HASH1>): MyIO(value='hello', attr=0), StringBuffer(_buffer=<_io.StringIO object at HASH2>): MyIO(value='result', attr=0)}

```