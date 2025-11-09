## Resource

```python
# Captures that the same IO can have more than one (shared) resource:
from dataclasses import dataclass
from pathlib import Path

from ordeq_files import CSV


@dataclass(frozen=True)
class Partition:
    idx: str


partition_nl = Partition("NL")
partition_be = Partition("BE")
partition_eu = Partition("Europe")
folder = Path("folder")

csv_nl = CSV(path=folder / Path(partition_nl.idx)) @ partition_nl
csv_be = CSV(path=folder / Path(partition_be.idx)) @ partition_be
csv_nl.with_resource(partition_eu)
csv_be.with_resource(partition_eu)

print(csv_nl.resource)
print(csv_be.resource)

```

## Output

```text
Partition(idx='Europe')
Partition(idx='Europe')

```

## Logging

```text
WARNING	ordeq.io	The syntax 'IO @ resource' is in preview mode and may change without notice in future releases.
WARNING	ordeq.io	The syntax 'IO @ resource' is in preview mode and may change without notice in future releases.

```