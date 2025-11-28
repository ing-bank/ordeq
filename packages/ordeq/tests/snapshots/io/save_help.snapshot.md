## Resource

```python
from dataclasses import dataclass
from pathlib import Path

from ordeq import Output


@dataclass(kw_only=True, frozen=True)
class ExampleOutputsaveArg(Output):
    path: Path
    attribute: str

    def save(self, data: str) -> None:
        """Save docstring

        Args:
            data: string to compare to
        """
        assert data == f"{self.path}@{self.attribute}: Hello world!"


example_output = ExampleOutputsaveArg(path=Path("hello.txt"), attribute="L1")
# re-enable when Py3.11+ is the minimum version
# help(example_output.save)  # noqa: ERA001

```