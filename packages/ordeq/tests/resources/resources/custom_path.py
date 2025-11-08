# Captures how resources can be used to distinguish between two IO
# distinct implementations that both consume from a file, but are
# initialized differently.
from dataclasses import dataclass
from pathlib import Path

from ordeq import Input
from ordeq_files import CSV, Text


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
csv_raw = CSV(path=path) @ path
csv_text = Text(path=path) @ path
custom1 = CustomIO(uri=path.as_uri()) @ path
custom2 = CustomIO2(file=str(path), py_file=path.suffix == ".py") @ path
print(csv_raw.resources)
print(csv_text.resources)
print(custom1)
print(custom1.resources)
print(custom2)
print(custom2.resources)
