## Resource

```python
from example_catalogs import local, remote
from example_catalogs.remote import hello
from ordeq._substitute import _substitutes_modules_to_ios
from ordeq_common import Print

print(_substitutes_modules_to_ios({local: remote, hello: Print()}))

```

## Output

```text
{StringBuffer(_buffer=<_io.StringIO object at HASH1>): StringBuffer(_buffer=<_io.StringIO object at HASH2>), StringBuffer(_buffer=<_io.StringIO object at HASH3>): StringBuffer(_buffer=<_io.StringIO object at HASH4>), StringBuffer(_buffer=<_io.StringIO object at HASH2>): Print()}

```