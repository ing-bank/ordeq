import difflib
import importlib.util
import logging
import re
from pathlib import Path

import pytest
from mypy import api as mypy_api

PACKAGE_DIR = Path(__file__).resolve().parent
RESOURCE_DIR = PACKAGE_DIR / "resources"
SNAPSHOT_DIR = PACKAGE_DIR / "snapshots"

FILES = list(RESOURCE_DIR.rglob("*.py"))


def _replace_pattern_with_seq(text: str, pattern: str, prefix: str) -> str:
    """Replace unique matches of pattern with prefix1, prefix2, ..."""
    seen = {}
    for match in re.finditer(pattern, text):
        val = match.group(0)
        if val not in seen:
            seen[val] = f"{prefix}{len(seen) + 1}"

    def repl(m):
        return seen[m.group(0)]

    return re.sub(pattern, repl, text)


def replace_object_hashes(text: str) -> str:
    """Replace object hashes like 0x103308890 with HASH1, HASH2, etc."""
    return _replace_pattern_with_seq(text, r"0x[0-9a-fA-F]+", "HASH")


def replace_uuid4(text: str) -> str:
    """Replace UUID4 strings with ID1, ID2, etc."""
    return _replace_pattern_with_seq(
        text,
        r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}",
        "ID",
    )


@pytest.mark.parametrize(
    "file_path",
    FILES,
    ids=[str(file.relative_to(RESOURCE_DIR)) for file in FILES],
)
def test_resources(file_path: Path, capsys, caplog) -> None:
    caplog.set_level(logging.INFO)
    caplog.handler.setFormatter(
        logging.Formatter(fmt="%(levelname)s\t%(name)s\t%(message)s")
    )

    snapshot_path = SNAPSHOT_DIR / file_path.relative_to(RESOURCE_DIR)
    snapshot_path.parent.mkdir(parents=True, exist_ok=True)
    snapshot_path = snapshot_path.with_suffix(".snapshot")

    # Dynamically import the module
    spec = importlib.util.spec_from_file_location(file_path.stem, file_path)
    module = importlib.util.module_from_spec(spec)

    sections = {}
    try:
        spec.loader.exec_module(module)
    except Exception as e:
        sections["Exception"] = f"{type(e).__name__}: {e}"

    captured_out_err = capsys.readouterr()
    if captured_out_err.out:
        sections["Output"] = captured_out_err.out
    if captured_out_err.err:
        sections["Error"] = captured_out_err.err
    if caplog.text:
        sections["Logging"] = caplog.text

    type_out, _, exit_code = mypy_api.run([str(file_path)])
    if exit_code != 0:
        sections["Typing"] = type_out

    output = "\n\n".join(
        f"{key}:\n{value.rstrip()}" for key, value in sections.items()
    )

    # Normalize object hashes
    captured = replace_uuid4(replace_object_hashes(output))

    # Read snapshot
    expected = (
        snapshot_path.read_text() if snapshot_path.exists() else "<NONE>"
    )
    expected = replace_object_hashes(expected)

    # Compare and write diff if not equal
    if captured != expected:
        diff = "\n".join(
            difflib.unified_diff(
                expected.splitlines(),
                captured.splitlines(),
                fromfile="expected",
                tofile="actual",
            )
        )
        snapshot_path.with_suffix(".snapshot").write_text(captured)
        pytest.fail(f"Output does not match snapshot:\n{diff}")
