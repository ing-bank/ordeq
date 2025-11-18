import tempfile
import typing
from pathlib import Path

import pandas as pd
from ordeq import IO, node, run
from ordeq_common import Literal
from ordeq_files import JSON
from ordeq_viz import viz

records = Literal(
    pd.DataFrame({"id": [1, 2, 3, 4], "value": [10, -5, 20, -1]})
)
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
