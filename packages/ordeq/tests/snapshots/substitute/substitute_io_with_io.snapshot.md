## Resource

```python
from ordeq._substitute import _build_substitution_map

from ordeq import IO
from ordeq_common import BytesBuffer

buffer = BytesBuffer()

print(_build_substitution_map({buffer: IO()}))

```

## Output

```text
{BytesBuffer(_buffer=<_io.BytesIO object at HASH1>): IO(idx=ID1)}

```