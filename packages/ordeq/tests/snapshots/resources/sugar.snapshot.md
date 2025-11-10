## Resource

```python
# Shows sugarcoated syntax to add a resource
from pathlib import Path

from ordeq._io import get_resource
from ordeq_files import CSV, Text

resource = 1234
csv = CSV(path=Path("my_path")) @ resource
csv_text = Text(path=Path("my_path")) @ resource
print(get_resource(csv))
print(get_resource(csv_text))

```

## Output

```text
1234
1234

```

## Logging

```text
WARNING	ordeq.io	Resources are in preview mode and may change without notice in future releases.
WARNING	ordeq.io	Resources are in preview mode and may change without notice in future releases.

```