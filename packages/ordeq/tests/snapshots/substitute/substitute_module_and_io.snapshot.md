## Resource

```python
from ordeq._substitute import _build_substitution_map

from example_catalogs import local, remote
from example_catalogs.remote import hello
from ordeq_common import Print

print(_build_substitution_map({local: remote, hello: Print()}))

```

## Output

```text
{StringBuffer(_buffer=<_io.StringIO object at HASH1>): StringBuffer(_buffer=<_io.StringIO object at HASH2>), StringBuffer(_buffer=<_io.StringIO object at HASH3>): StringBuffer(_buffer=<_io.StringIO object at HASH4>), StringBuffer(_buffer=<_io.StringIO object at HASH2>): Print()}

```