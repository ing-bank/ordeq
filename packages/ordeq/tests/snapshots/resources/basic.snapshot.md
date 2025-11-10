## Resource

```python
# Captures basic behaviour of resources
from pathlib import Path

from ordeq._io import get_resource
from ordeq_files import CSV, Text

resource = 0.1244
csv = CSV(path=Path("my/path")).with_resource(resource)
csv_text = Text(path=Path("my/path")).with_resource(resource)
print(get_resource(csv))
print(get_resource(csv_text))

```

## Output

```text
0.1244
0.1244

```

## Logging

```text
WARNING	ordeq.io	Resources are in preview mode and may change without notice in future releases.
WARNING	ordeq.io	Resources are in preview mode and may change without notice in future releases.

```