# Shows syntax to auto-initialize an IO from on the resource attributes.

import pathlib
from typing import TypeVar

from ordeq import Resource
from ordeq._io import AnyIO
from ordeq._resource import get_resources
from ordeq_files import CSV, Text

T = TypeVar("T", bound=AnyIO)


class Path(Resource, pathlib.Path):
    def create_io(self, io: type[T]) -> T:
        io = io(path=self)
        self.add_io(io)
        return io

    def __gt__(self, io: type[T]) -> T:
        return self.create_io(io)


path = Path("some/file.csv")
csv_raw = path.create_io(CSV)
csv_text = path > Text

print(csv_raw)
print(csv_text)
print(get_resources(csv_raw))
print(get_resources(csv_text))
