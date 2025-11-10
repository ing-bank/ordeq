## Resource

```python
# Shows potential syntax that allows IO implementations to define the default
# resources consumed by the IO. This may be useful since many times the
# resource of the IO can be inferred directly from one of its attributes.
from dataclasses import dataclass
from pathlib import Path

from ordeq import Input
from ordeq._io import get_resource


@dataclass(frozen=True)
class CSV(Input[str]):
    path: Path

    def load(self) -> str:
        return str(self.path)


csv = CSV(path=Path("file"))

resource = "my-resource"
file_overridden = CSV(path=Path("overridden")) @ resource
file_extended = csv @ resource

print(get_resource(csv))
print(get_resource(file_overridden))
print(get_resource(file_extended))

```

## Output

```text
CSV(path=Path('file'))
my-resource
my-resource

```

## Logging

```text
WARNING	ordeq.io	The syntax 'IO @ resource' is in preview mode and may change without notice in future releases.
WARNING	ordeq.io	The syntax 'IO @ resource' is in preview mode and may change without notice in future releases.

```