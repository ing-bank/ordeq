## Resource

```python
from ordeq_common import StringBuffer
from typing_extensions import reveal_type

s = StringBuffer("Hello, World!")

reveal_type(s._saver)
print(s._saver("~/.',.`#"))
print(s.load())

```

## Output

```text
~/.',.`#
Hello, World!~/.',.`#

```

## Error

```text
Runtime type is 'View'

```

## Logging

```text
INFO	ordeq.io	Saving StringBuffer(_buffer=<_io.StringIO object at HASH1>)
INFO	ordeq.io	Loading StringBuffer(_buffer=<_io.StringIO object at HASH1>)

```