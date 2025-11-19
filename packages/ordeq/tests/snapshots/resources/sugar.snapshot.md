## Resource

```python
# Shows sugarcoated syntax to add a resource
from pathlib import Path

from ordeq_files import CSV, Text

resource = 1234
csv = CSV(path=Path("my_path")) @ resource
csv_text = Text(path=Path("my_path")) @ resource
print(csv._resource)
print(csv_text._resource)

```

## Output

```text
1234
1234

```

## Logging

```text
WARNING	ordeq.preview	Resources are in preview mode and may change without notice in future releases.
WARNING	ordeq.preview	Resources are in preview mode and may change without notice in future releases.

```