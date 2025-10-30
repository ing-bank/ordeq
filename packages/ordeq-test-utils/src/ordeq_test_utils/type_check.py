from pathlib import Path

from mypy import api as mypy_api

from ordeq_test_utils.snapshot import compare


def capture_type_check(path: Path) -> str:
    """Captures the type check output of the given path using mypy.

    Args:
        path: The path to type check.

    Returns:
        The type check output as a string.
    """
    stdout, _, exit_code = mypy_api.run([str(path)])
    if exit_code != 0:
        return stdout
    return "No type errors found."


def capture_type_check_and_compare(
    capture: Path, snapshot: Path
) -> str | None:
    """Captures the type check output of the given path and compares it against
    the snapshot.

    Args:
        capture: The path to capture type check output from.
        snapshot: The path to the snapshot file to compare against.

    Returns:
        A diff string if there are differences, otherwise None.
    """
    captured = capture_type_check(capture)
    expected = (
        snapshot.read_text(encoding="utf-8") if snapshot.exists() else "<NONE>"
    )
    if captured != expected:
        diff = compare(captured, expected)
        snapshot.parent.mkdir(parents=True, exist_ok=True)
        snapshot.write_text(captured, encoding="utf-8", newline="\n")
        return diff
    return None
