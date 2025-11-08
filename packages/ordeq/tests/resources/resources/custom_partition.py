# Captures that the same IO can have more than one (shared) resource:
from dataclasses import dataclass
from pathlib import Path

from ordeq import Resource
from ordeq._resource import get_resources
from ordeq_files import CSV


@dataclass(frozen=True)
class Partition(Resource):
    idx: str


partition_nl = Partition("NL")
partition_be = Partition("BE")
partition_eu = Partition("Europe")
folder = Path("folder")

csv_nl = partition_nl.add_io(CSV(path=folder / Path(partition_nl.idx)))
csv_be = partition_be.add_io(CSV(path=folder / Path(partition_be.idx)))
partition_eu.add_io(csv_nl)
partition_eu.add_io(csv_be)

print(get_resources(csv_nl))
print(get_resources(csv_be))
