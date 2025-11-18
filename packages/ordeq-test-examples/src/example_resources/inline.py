from collections.abc import Generator
from pathlib import Path

from ordeq import node
from ordeq_files import CSV, Text

path = Path("data1.csv")


@node(outputs=CSV(path=path) @ path)
def generate() -> Generator:
    yield ["constant", "idx"]
    for idx in range(4):
        yield [1, idx]


@node(inputs=Text(path=path) @ path)
def consume(data: str) -> None:
    print(data)
