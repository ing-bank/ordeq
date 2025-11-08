# Shows potential syntax that allows IO implementations to define the default
# resources consumed by the IO. This may be useful since many times the resource
# of the IO can be inferred directly from one of its attributes.
from dataclasses import dataclass
from pathlib import Path

from ordeq import Input
from ordeq._resource import Resource, get_resources


class File:
    path: Path

    def __resources__(self) -> set:
        return {self.path}


@dataclass(frozen=True)
class CSV(Input[str], File):
    path: Path

    def load(self) -> str:
        return str(self.path)


csv = CSV(path=Path("file"))

print(get_resources(csv))

resource = Resource()
file_overridden = resource.add_io(CSV(path=Path("overridden")))
file_extended = resource.add_io(csv)
