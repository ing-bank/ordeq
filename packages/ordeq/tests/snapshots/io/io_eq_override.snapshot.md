## Resource

```python
from ordeq import IO


class CustomIO(IO):
    def __init__(self, attr: str):
        super().__init__()
        self.attr = attr

    def load(self) -> str:
        return self.attr

    def save(self, data: str) -> None:
        print(data)

    def __eq__(self, other) -> bool:
        return isinstance(other, CustomIO) and self.attr == other.attr

    def __hash__(self) -> int:
        return hash(self.attr)


a = CustomIO("a")
b = CustomIO("b")

assert a is not b
assert a != b
assert hash(a) != hash(b)

B = CustomIO("b")

assert b is not B
assert b != B
assert hash(b) != hash(B)

```