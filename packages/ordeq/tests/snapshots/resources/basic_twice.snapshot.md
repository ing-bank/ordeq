## Resource

```python
# Captures behaviour when one IO is added twice to the same resource
from pathlib import Path

from ordeq._io import get_resource
from ordeq_files import CSV

resource = "resource!"
csv = CSV(path=Path("my/path")).with_resource(resource)
csv_twice = csv.with_resource(resource)
print(get_resource(csv))
print(get_resource(csv_twice))

```

## Output

```text
resource!
resource!

```