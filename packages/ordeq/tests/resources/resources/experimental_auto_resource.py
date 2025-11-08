# Shows syntax to derive a resource based from an IO attribute.
# This is useful in scenarios where the resource can directly be
# inferred from the IO attributes.
from dataclasses import dataclass
from pathlib import Path
from typing import Any, TypeVar, overload

from ordeq._io import AnyIO, Input
from ordeq._resource import Resource, get_resources

T = TypeVar("T", bound=AnyIO)


@dataclass(frozen=True)
class ValuedResource(Resource):
    any: Any


@dataclass(frozen=True)
class File(Input[str]):
    path: Path

    def load(self) -> str:
        return self.path.read_text()

    @overload
    def __matmul__(self, resource: str) -> "File": ...

    @overload
    def __matmul__(self, resource: Resource) -> "File": ...

    def __matmul__(self, resource: Resource | str) -> "File":
        if isinstance(resource, str):
            return ValuedResource(getattr(self, resource)).add_io(self)
        return resource.add_io(self)


file = Path("some/file.csv")
csv_raw = File(path=file) @ "path"

print(csv_raw)
print(get_resources(csv_raw))
