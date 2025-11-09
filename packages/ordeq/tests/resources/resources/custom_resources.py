# Shows potential syntax that allows IO implementations to define the default
# resources consumed by the IO. This may be useful since many times the resource
# of the IO can be inferred directly from one of its attributes.
from dataclasses import dataclass
from pathlib import Path

from ordeq import Input


@dataclass(frozen=True)
class CSV(Input[str]):
    path: Path

    def load(self) -> str:
        return str(self.path)


csv = CSV(path=Path("file"))

resource = "my-resource"
file_overridden = CSV(path=Path("overridden")) @ resource
file_extended = csv @ resource

print(csv.resource)
print(file_overridden.resource)
print(file_extended.resource)
