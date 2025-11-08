from dataclasses import dataclass

from ordeq import Input, Resource
from ordeq._resource import get_resources


@dataclass(frozen=True)
class IcebergTable(Resource):
    catalog: str
    ns: str
    name: str


@dataclass(frozen=True)
class PyIcebergTable(Input[None]):
    catalog: str
    ns: str
    table: str

    def load(self) -> None: ...


@dataclass(frozen=True)
class SparkIcebergTable(Input[None]):
    table: str

    def load(self) -> None: ...


tbl = IcebergTable(catalog="global", ns="acc", name="txs")
csv = tbl.add_io(
    PyIcebergTable(catalog=tbl.catalog, ns=tbl.ns, table=tbl.name)
)
csv_text = tbl.add_io(
    SparkIcebergTable(table=f"{tbl.catalog}.{tbl.ns}.{tbl.name}")
)
print(get_resources(csv))
print(get_resources(csv_text))
