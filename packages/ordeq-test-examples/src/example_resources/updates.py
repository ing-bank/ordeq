from collections.abc import Generator
from pathlib import Path

from ordeq import node
from ordeq_common import Print
from ordeq_files import CSV

csv = CSV(path=Path("data3.csv"))
csv_old = csv @ "old"
csv_new = csv @ "new"


@node(inputs=csv_old, outputs=csv_new)
def update(data: tuple) -> Generator:
    yield ["constant", "idx"]
    for item in data:
        yield [f"{item[0]} (updated)", item[1]]


@node(inputs=csv_new, outputs=Print())
def reflect(data: tuple) -> None:
    print("Updated:")
    for item in data:
        print(item)
