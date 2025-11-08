## Resource

```python
# Captures how resources can be used to distinguish between two IO
# distinct implementations that both consume an Iceberg table.
from dataclasses import dataclass

from ordeq import Input


@dataclass(frozen=True)
class IcebergTable:
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
py = PyIcebergTable(catalog=tbl.catalog, ns=tbl.ns, table=tbl.name) @ tbl
sp = SparkIcebergTable(table=f"{tbl.catalog}.{tbl.ns}.{tbl.name}") @ tbl
print(py.resources)
print(sp.resources)

```

## Output

```text
{IcebergTable(catalog='global', ns='acc', name='txs')}
{IcebergTable(catalog='global', ns='acc', name='txs')}

```