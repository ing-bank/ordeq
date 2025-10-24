from pathlib import Path

import pytest
from ordeq_test_utils import compare_resources_against_snapshots

TESTS_DIR = Path(__file__).resolve().parent
RESOURCE_DIR = TESTS_DIR / "resources"
SNAPSHOT_DIR = TESTS_DIR / "snapshots"


@pytest.mark.parametrize(
    ("file_path", "snapshot_path"),
    [
        pytest.param(
            file_path,
            SNAPSHOT_DIR
            / file_path.relative_to(RESOURCE_DIR).with_suffix(".snapshot.md"),
            id=str(file_path.relative_to(RESOURCE_DIR)),
        )
        for file_path in RESOURCE_DIR.rglob("*.py")
    ],
)
def test_resource(
    file_path: Path, snapshot_path: Path, capsys, caplog
) -> None:
    diff = compare_resources_against_snapshots(
        file_path, snapshot_path, caplog, capsys
    )
    if diff:
        pytest.fail(f"Output does not match snapshot:\n{diff}")
