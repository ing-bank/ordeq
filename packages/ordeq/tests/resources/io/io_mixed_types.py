# Captures loading and saving an IO with different load and save type.
# This example is highly artificial and should not be used as a reference when
# implementing IOs in practice.
from dataclasses import dataclass

from ordeq import Input, Output


@dataclass(kw_only=True, frozen=True)
class ExampleIO(Input[str], Output[int]):
    attribute: str

    def load(self) -> str:
        return str(self.attribute)

    def save(self, length: int) -> None:
        print(length)

    def __repr__(self):
        # To clean the output
        return "Text"


example = ExampleIO(attribute="L1")
print(f"Should print {example.attribute}:")
print(example.load())
print("Should print 10:")
example.save(10)
