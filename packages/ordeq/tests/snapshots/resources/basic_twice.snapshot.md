## Resource

```python
# Captures behaviour when one IO is added twice to the same resource
from pathlib import Path

from ordeq_files import CSV

resource = "resource!"
csv = CSV(path=Path("my/path")).with_resource(resource)
csv_twice = csv.with_resource(resource)
print(csv.resources)
print(csv_twice.resources)

```

## Output

```text
{'resource!'}
{'resource!'}

```