## Resource

```python
# Captures basic behaviour of resources
from pathlib import Path

from ordeq_files import CSV, Text

resource = 0.1244
csv = CSV(path=Path("my/path")).with_resource(resource)
csv_text = Text(path=Path("my/path")).with_resource(resource)
print(csv._resource)
print(csv_text._resource)

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