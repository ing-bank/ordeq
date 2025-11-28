from dataclasses import dataclass
from pathlib import Path

from ordeq import Output


@dataclass(kw_only=True, frozen=True)
class ExampleOutputsaveArg(Output):
    path: Path
    attribute: str

    def save(self, data: str) -> None:
        assert data == f"{self.path}@{self.attribute}: Hello world!"


example_output = ExampleOutputsaveArg(path=Path("hello.txt"), attribute="L1")
example_output.save("hello.txt@L1: Hello world!")
