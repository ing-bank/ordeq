from collections.abc import Generator
from pathlib import Path

from ordeq import node
from ordeq_files import CSV, Text

path = Path("data2.csv")
csv = CSV(path=path) @ path
text = Text(path=path) @ path


@node(outputs=csv)
def generate() -> Generator:
    yield ["constant", "idx"]
    for idx in range(4):
        yield [1, idx]


@node(inputs=text)
def consume(data: str) -> None:
    print(data)
