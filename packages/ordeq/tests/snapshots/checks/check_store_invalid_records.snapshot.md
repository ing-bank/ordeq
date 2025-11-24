## Resource

```python
import tempfile
import typing
from pathlib import Path

import pandas as pd
from ordeq import IO, Input, node, run
from ordeq_files import JSON
from ordeq_viz import viz

records = Input(pd.DataFrame({"id": [1, 2, 3, 4], "value": [10, -5, 20, -1]}))
invalid_records = JSON(
    path=Path(tempfile.gettempdir()) / "invalid_records.json"
)
processed_records = IO()


@node(inputs=records)
def process_records(rows: pd.DataFrame) -> pd.DataFrame:
    rows["processed_value"] = rows["value"] * 2
    return rows


@node(inputs=records, outputs=invalid_records, checks=records)
def check_store_invalid_records(rows: pd.DataFrame) -> dict[str, typing.Any]:
    invalids = rows.where(rows["value"] < 0)
    status: typing.Literal["failed", "passed"] = (
        "failed" if not invalids.empty else "passed"
    )
    return {"status": status, "records": invalids.to_json()}


@node(inputs=invalid_records)
def print_invalid_records(report: dict[str, typing.Any]) -> None:
    print("Invalid Records Check Status:", report["status"])
    if report["status"] == "failed":
        print("Invalid Records Data:", report["records"])


@node(inputs=process_records)
def print_processed_records(rows: pd.DataFrame) -> None:
    print("Processed Records Data:", rows.to_json())


if __name__ == "__main__":
    print(viz(__name__, fmt="mermaid"))
    run(__name__)

```

## Output

```text
graph TB
	subgraph legend["Legend"]
		direction TB
		L0@{shape: rounded, label: "Node"}
		L2@{shape: subroutine, label: "View"}
		L00@{shape: rect, label: "IO"}
		L01@{shape: rect, label: "Input"}
		L02@{shape: rect, label: "JSON"}
	end

	IO0 --> __main__:check_store_invalid_records
	__main__:check_store_invalid_records --> IO1
	IO0 --> __main__:process_records
	__main__:process_records --> __main__:print_processed_records
	IO1 --> __main__:print_invalid_records

	__main__:check_store_invalid_records@{shape: rounded, label: "check_store_invalid_records"}
	__main__:process_records@{shape: subroutine, label: "process_records"}
	__main__:print_processed_records@{shape: subroutine, label: "print_processed_records"}
	__main__:print_invalid_records@{shape: subroutine, label: "print_invalid_records"}
	IO1@{shape: rect, label: "invalid_records"}
	IO0@{shape: rect, label: "records"}

	class L0,__main__:check_store_invalid_records node
	class L2,__main__:process_records,__main__:print_processed_records,__main__:print_invalid_records view
	class L00 io0
	class L01,IO0 io1
	class L02,IO1 io2
	classDef node fill:#008AD7,color:#FFF
	classDef io fill:#FFD43B
	classDef view fill:#00C853,color:#FFF
	classDef io0 fill:#66c2a5
	classDef io1 fill:#fc8d62
	classDef io2 fill:#8da0cb

Processed Records Data: {"id":{"0":1,"1":2,"2":3,"3":4},"value":{"0":10,"1":-5,"2":20,"3":-1},"processed_value":{"0":20,"1":-10,"2":40,"3":-2}}
Invalid Records Check Status: failed
Invalid Records Data: {"id":{"0":null,"1":2.0,"2":null,"3":4.0},"value":{"0":null,"1":-5.0,"2":null,"3":-1.0}}

```

## Logging

```text
WARNING	ordeq.preview	Checks are in preview mode and may change without notice in future releases.
INFO	ordeq.runner	Running node 'check_store_invalid_records' in module '__main__'
INFO	ordeq.io	Saving JSON(path=Path('<TEMP_DIR>/invalid_records.json'))
INFO	ordeq.runner	Running view 'process_records' in module '__main__'
INFO	ordeq.runner	Running view 'print_processed_records' in module '__main__'
INFO	ordeq.runner	Running view 'print_invalid_records' in module '__main__'

```