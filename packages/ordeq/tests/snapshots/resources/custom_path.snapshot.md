## Resource

```python
# Captures how resources can be used to distinguish between two IO
# distinct implementations that both consume from a file, but are
# initialized differently.
from pathlib import Path
from dataclasses import dataclass

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

```

## Output

```text
{Path('/packages/ordeq/tests/resources/resources/custom_path.py')}
{Path('/packages/ordeq/tests/resources/resources/custom_path.py')}
CustomIO(uri='file:///packages/ordeq/tests/resources/resources/custom_path.py')
{Path('/packages/ordeq/tests/resources/resources/custom_path.py')}
CustomIO2(file='/packages/ordeq/tests/resources/resources/custom_path.py', py_file=True)
{Path('/packages/ordeq/tests/resources/resources/custom_path.py')}

```