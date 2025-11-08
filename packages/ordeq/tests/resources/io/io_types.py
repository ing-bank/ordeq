# Captures loading and saving an IO with different load and save type.
from dataclasses import dataclass

from ordeq import IO


@dataclass(kw_only=True, frozen=True)
class ExampleIO(IO[str, int]):
    attribute: str

    def load(self) -> str:
        return str(self)

    def save(self, length: int) -> None:
        print(self, length)

    def __repr__(self):
        # To clean the output
        return "Text"


example = ExampleIO(attribute="L1")
print(example.load())
example.save(10)
