## Resource

```python
from typing_extensions import reveal_type

from ordeq_common import StringBuffer

s = StringBuffer("Hello, World!")

reveal_type(s._loader)
print(s._loader)
print(s._loader())

```

## Output

```text
View(func=ordeq_common.io.string_buffer:load, ...)
Hello, World!

```

## Error

```text
Runtime type is 'View'

```

## Logging

```text
INFO	ordeq.io	Loading StringBuffer(_buffer=<_io.StringIO object at HASH1>)

```