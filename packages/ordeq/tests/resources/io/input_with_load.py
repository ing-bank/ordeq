from dataclasses import dataclass
from pathlib import Path

from ordeq import Input


@dataclass(kw_only=True, frozen=True)
class ExampleInputLoadArg(Input[str]):
    path: Path
    attribute: str

    def load(self) -> str:
        return f"{self.path}@{self.attribute}: Hello world!"


example_input = ExampleInputLoadArg(path=Path("hello.txt"), attribute="L1")
print(example_input.load())
