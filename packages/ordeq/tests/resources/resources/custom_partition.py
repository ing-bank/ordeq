# Captures that the same IO can have more than one (shared) resource:
from dataclasses import dataclass
from pathlib import Path

from ordeq_files import CSV


@dataclass(frozen=True)
class Partition:
    idx: str


partition_nl = Partition("NL")
partition_be = Partition("BE")
partition_eu = Partition("Europe")
folder = Path("folder")

csv_nl = CSV(path=folder / Path(partition_nl.idx)) @ partition_nl
csv_be = CSV(path=folder / Path(partition_be.idx)) @ partition_be

print(csv_nl._resource)
print(csv_be._resource)
