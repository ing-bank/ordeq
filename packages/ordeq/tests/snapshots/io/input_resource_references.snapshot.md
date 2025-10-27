## Resource

```python
# This resource reflects how __resources__ behaves in inheritance scenarios.
# The resources of the child class should be concatenated with those of the
# parent class.
from dataclasses import dataclass

from ordeq import Input
from ordeq_common import Literal
from ordeq._io import _get_resources


@dataclass(kw_only=True, frozen=True)
class Referencing(Input[str]):
    attr: str
    io: Input[str]

    def load(self) -> str:
        return self.attr + self.io.load()

    def __resources__(self) -> list[str]:
        return [self.attr]


referencing = Referencing(attr="Hello", io=Literal[str]("world"))
referencing_self = Referencing(attr="Buenos", io=referencing)
referencing_referencing_self = Referencing(attr="Hola", io=referencing_self)

print(_get_resources(referencing))
print(_get_resources(referencing_self))
print(_get_resources(referencing_referencing_self))

```

## Output

```text
['Hello']
['Buenos', 'Hello']
['Hola', 'Buenos', 'Hello']

```