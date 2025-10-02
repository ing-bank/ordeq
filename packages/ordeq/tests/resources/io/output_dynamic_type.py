from dataclasses import dataclass

from ordeq import Output

from ordeq import node
from typing import TypeVar

T = TypeVar("T", bound=str | int)


@dataclass(frozen=True)
class DynamicType(Output[T]):
    def save(self, data: T) -> None:
        if isinstance(data, int):
            print(self, 'int:', data)
        print(self, 'str:', data)


number = DynamicType[int]()
number.save(42)
string = DynamicType[str]()
string.save("hello")

io = DynamicType()


@node(outputs=io)
def create_int() -> int:
    return 101


@node(outputs=io)
def create_str() -> str:
    return "foo"
