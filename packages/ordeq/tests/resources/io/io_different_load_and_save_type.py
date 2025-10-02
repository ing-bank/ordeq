from dataclasses import dataclass

from ordeq import Output, Input

from ordeq import node
from typing import TypeVar


class DifferentLoadAndSaveType(Input[str], Output[int]):
    def load(self) -> str:
        return "hello!"

    def save(self, data: int) -> None:
        print(self, 'data:', data)


io = DifferentLoadAndSaveType()
print(io.load())
io.save(101)
