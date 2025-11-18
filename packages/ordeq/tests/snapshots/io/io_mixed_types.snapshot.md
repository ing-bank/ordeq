## Resource

```python
# Captures loading and saving an IO with different load and save type.
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

```

## Output

```text
Should print L1:
L1
Should print 10:
10

```

## Logging

```text
INFO	ordeq.io	Loading Text
INFO	ordeq.io	Saving Text

```