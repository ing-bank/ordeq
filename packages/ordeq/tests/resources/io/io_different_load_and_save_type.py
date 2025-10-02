from dataclasses import dataclass

from ordeq import Output, Input

from ordeq import node
from typing import TypeVar


# Allowing load type to be different from save type could ease integration with
# Redis, SQLAlchemy, BigQuery. The Python client libraries for these services
# return a different type on load/read than they accept on save/write.
class DifferentLoadAndSaveType(Input[str], Output[int]):
    def load(self) -> str:
        return "hello!"

    def save(self, data: int) -> None:
        print(self, 'data:', data)


io = DifferentLoadAndSaveType()
print(io.load())
io.save(101)
