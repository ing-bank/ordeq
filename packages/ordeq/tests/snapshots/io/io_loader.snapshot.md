## Resource

```python
from ordeq_common import StringBuffer
from typing_extensions import reveal_type

s = StringBuffer("Hello, World!")

reveal_type(s._loader)
print(s._loader)
print(s._loader())

```

## Output

```text
StringBuffer(_buffer=<_io.StringIO object at HASH1>)
Hello, World!

```

## Error

```text
Runtime type is 'Loader'

```

## Logging

```text
INFO	ordeq.io	Loading StringBuffer(_buffer=<_io.StringIO object at HASH1>)

```