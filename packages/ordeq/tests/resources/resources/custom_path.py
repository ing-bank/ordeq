# Captures how resources can be used to distinguish between two IO
# distinct implementations that both consume from a file, but are
# initialized differently.
import pathlib
from dataclasses import dataclass

from ordeq import Input, Resource
from ordeq._resource import get_resources
from ordeq_files import CSV, Text


class Path(Resource, pathlib.Path): ...


@dataclass(frozen=True)
class CustomIO(Input[None]):
    # Takes only URI, not a regular Path
    uri: str

    def load(self) -> None: ...


@dataclass(frozen=True)
class CustomIO2(Input[None]):
    file: str
    py_file: bool

    def load(self) -> None: ...


path = Path(__file__).resolve()
csv_raw = path.add_io(CSV(path=path))
csv_text = path.add_io(Text(path=path))
custom1 = path.add_io(CustomIO(uri=path.as_uri()))
custom2 = path.add_io(CustomIO2(file=str(path), py_file=path.suffix == ".py"))
print(get_resources(csv_raw))
print(get_resources(csv_text))
print(custom1)
print(get_resources(custom1))
print(custom2)
print(get_resources(custom2))
