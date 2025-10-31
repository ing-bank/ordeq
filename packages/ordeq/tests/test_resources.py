from pathlib import Path

import pytest
from ordeq_test_utils import (
    capture_type_check_and_compare,
    compare_resources_against_snapshots,
)

TESTS_DIR = Path(__file__).resolve().parent
RESOURCE_DIR = TESTS_DIR / "resources"
SNAPSHOT_DIR = TESTS_DIR / "snapshots"


@pytest.mark.snapshot
@pytest.mark.parametrize(
    ("file_path", "snapshot_path"),
    [
        pytest.param(
            file_path,
            SNAPSHOT_DIR
            / file_path.relative_to(RESOURCE_DIR).with_suffix(".snapshot.md"),
            id=str(file_path.relative_to(RESOURCE_DIR)),
        )
        for file_path in sorted(RESOURCE_DIR.rglob("*.py"))
    ],
)
def test_resource(
    file_path: Path, snapshot_path: Path, capsys, caplog, recwarn
) -> None:
    diff = compare_resources_against_snapshots(
        file_path, snapshot_path, caplog, capsys, recwarn
    )
    if diff:
        pytest.fail(f"Output does not match snapshot:\n{diff}")


@pytest.mark.snapshot
def test_typing():
    diff = capture_type_check_and_compare(
        RESOURCE_DIR, SNAPSHOT_DIR / "typing.snapshot.md"
    )
    if diff:
        pytest.fail(f"Type check output does not match snapshot:\n{diff}")
