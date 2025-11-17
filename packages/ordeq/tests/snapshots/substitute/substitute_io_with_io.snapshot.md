## Resource

```python
from ordeq import IO
from ordeq._substitute import _substitutes_modules_to_ios
from ordeq_common import BytesBuffer

buffer = BytesBuffer()

print(_substitutes_modules_to_ios({buffer: IO()}))

```

## Output

```text
{BytesBuffer(_buffer=<_io.BytesIO object at HASH1>): IO(id=ID1)}

```