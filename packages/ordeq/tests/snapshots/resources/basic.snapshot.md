## Resource

```python
# Captures basic behaviour of resources
from pathlib import Path

from ordeq_files import CSV, Text

resource = 0.1244
csv = CSV(path=Path("my/path")).add_resource(resource)
csv_text = Text(path=Path("my/path")).add_resource(resource)
print(csv.resources)
print(csv_text.resources)

```

## Output

```text
{0.1244}
{0.1244}

```