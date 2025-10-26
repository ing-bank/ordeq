## Resource

```python
# This resource reflects how __resources__ behaves in inheritance scenarios.
# The resources of the child class should be concatenated with those of the
# parent class.
from dataclasses import dataclass

from ordeq import Input
from pathlib import Path
from ordeq._io import _get_resources


@dataclass(kw_only=True, frozen=True)
class Base(Input[str]):
    path: Path
    attr: str

    def load(self) -> str:
        return "Hello world"

    def __resources__(self) -> list[str]:
        return [self.attr]


f = Base(path=Path('my.file'), attr="base_value")
print(f.__resources__())


@dataclass(kw_only=True, frozen=True)
class Child(Base):
    path: Path

    def load(self) -> str:
        return "Hello world"

    def __resources__(self) -> list[str]:
        return [self.path.__fspath__()]


f = Child(path=Path('my.file'), attr="child_value")
print(f.__resources__())
print(_get_resources(f))

```

## Output

```text
['base_value']
['my.file']
['my.file', 'child_value']

```