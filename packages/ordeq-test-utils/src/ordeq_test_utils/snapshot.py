import difflib
import importlib.util
import logging
import re
import sys
from pathlib import Path

from _pytest.capture import CaptureFixture
from _pytest.logging import LogCaptureFixture
from mypy import api as mypy_api


def _replace_pattern_with_seq(text: str, pattern: str, prefix: str) -> str:
    """Replace unique matches of a regex pattern in the text with a sequential
    prefix.

    Args:
        text: The input string to process.
        pattern: The regex pattern to match in the text.
        prefix: The prefix to use for replacements (e.g., 'HASH', 'ID').

    Returns:
        The text with each unique match replaced by prefix1, prefix2, etc.
    """
    seen: dict[str, str] = {}
    for match in re.finditer(pattern, text):
        val = match.group(0)
        if val not in seen:
            seen[val] = f"{prefix}{len(seen) + 1}"

    def repl(m):
        return seen[m.group(0)]

    return re.sub(pattern, repl, text)


def replace_object_hashes(text: str) -> str:
    """Replace object hashes (e.g., 0x103308890) in the text with sequential
    placeholders.

    Args:
        text: The input string to process.

    Returns:
        The text with object hashes replaced by HASH1, HASH2, etc.
    """
    return _replace_pattern_with_seq(text, r"0x[0-9a-fA-F]+", "HASH")


def replace_uuid4(text: str) -> str:
    """Replace UUID4 strings in the text with sequential placeholders.

    Args:
        text: The input string to process.

    Returns:
        The text with UUID4 strings replaced by ID1, ID2, etc.
    """
    return _replace_pattern_with_seq(
        text,
        r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}",
        "ID",
    )


def run_module(file_path: Path) -> str | None:
    """Dynamically import and run a Python module from a file path.

    Args:
        file_path: The path to the Python file to import and run.

    Returns:
        None if the module runs successfully, otherwise a string describing
        the exception.
    """
    spec = importlib.util.spec_from_file_location(file_path.stem, file_path)
    if spec is None:
        return f"ImportError: Could not load spec for {file_path}"
    if spec.loader is None:
        return f"ValueError: Spec loader is None for {file_path}"
    module = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(module)
    except Exception as e:
        return f"{type(e).__name__}: {e}"
    return None


def make_output_invariant(output: str) -> str:
    """Normalize output to be invariant to UUIDs, object hashes, and
    OS-specific paths.

    Args:
        output: The captured output string to normalize.

    Returns:
        The normalized output string.
    """
    # Normalize object hashes
    captured = replace_uuid4(replace_object_hashes(output))

    # Normalize platform-specific paths
    return (
        captured.replace("PosixPath", "Path")
        .replace("WindowsPath", "Path")
        .replace("\\", "/")
    )


def _as_md_python_block(text: str) -> str:
    """Format a block of text as a Python code block in Markdown.

    Args:
        text: The text to format.

    Returns:
        the formatted text block.
    """

    return "```python\n" + text + "\n```"


def _as_md_text_block(text: str) -> str:
    """Format a block of text as a text code block in Markdown.

    Args:
        text: The text to format.

    Returns:
        the formatted text block.
    """

    return "```text\n" + text + "\n```"


def capture_module(
    file_path: Path, caplog: LogCaptureFixture, capsys: CaptureFixture
) -> str:
    """Capture the output, logging, errors, and typing feedback from running
    a Python module.

    Args:
        file_path: The path to the Python file to run.
        caplog: The pytest caplog fixture for capturing logs.
        capsys: The pytest capsys fixture for capturing stdout/stderr.

    Returns:
        The normalized captured output as a string.
    """
    caplog.set_level(logging.INFO)
    caplog.handler.setFormatter(
        logging.Formatter(fmt="%(levelname)s\t%(name)s\t%(message)s")
    )

    sections = {
        "Resource": _as_md_python_block(file_path.read_text(encoding="utf-8"))
    }

    exception = run_module(file_path)

    if exception is not None:
        sections["Exception"] = _as_md_text_block(exception)

    captured_out_err = capsys.readouterr()
    if captured_out_err.out:
        sections["Output"] = _as_md_text_block(captured_out_err.out)
    if captured_out_err.err:
        sections["Error"] = _as_md_text_block(captured_out_err.err)
    if caplog.text:
        sections["Logging"] = _as_md_text_block(caplog.text)

    # Add typing feedback
    type_out, _, exit_code = mypy_api.run([str(file_path)])
    if exit_code != 0:
        sections["Typing"] = _as_md_text_block(type_out)

    output = "\n\n".join(
        f"## {key}\n\n{value.rstrip()}" for key, value in sections.items()
    )

    return make_output_invariant(output)


def compare(captured: str, expected: str) -> str:
    """Return a unified diff between captured and expected strings.

    Args:
        captured: The actual captured output.
        expected: The expected output.

    Returns:
        A unified diff string showing the differences.
    """
    if captured == expected:
        return ""
    return "\n".join(
        difflib.unified_diff(
            expected.splitlines(),
            captured.splitlines(),
            fromfile="expected",
            tofile="actual",
        )
    )


def compare_resources_against_snapshots(
    file_path: Path,
    snapshot_path: Path,
    caplog: LogCaptureFixture,
    capsys: CaptureFixture,
) -> str | None:
    """Compare the output of a resource file against its snapshot, updating
    the snapshot if different.

    Args:
        file_path: The path to the resource file to test.
        snapshot_path: The path to the snapshot file to compare against.
        caplog: The pytest caplog fixture for capturing logs.
        capsys: The pytest capsys fixture for capturing stdout/stderr.

    Returns:
        A unified diff string if the outputs differ, otherwise None.
    """
    # Capture module output
    captured = capture_module(file_path, caplog, capsys)

    # Read expected content
    expected = (
        snapshot_path.read_text(encoding="utf-8")
        if snapshot_path.exists()
        else "<NONE>"
    )

    # Compare with snapshot and update if different
    if captured != expected:
        diff = compare(captured, expected)

        # Always write the snapshot file with normalized line endings
        snapshot_path.parent.mkdir(parents=True, exist_ok=True)
        snapshot_path.write_text(captured, encoding="utf-8", newline="\n")

        return diff
    return None


def append_packages_dir_to_sys_path(packages_dir: Path):
    """Append the packages directory to `sys.path`.

    This allows us to import the example packages at test time.
    Cleanup is performed after use to ensure a clean state for each test.

    Args:
        packages_dir: The path to the packages directory.

    """
    sys.path.append(str(packages_dir))
    yield
    sys.path.remove(str(packages_dir))

    # Cleanup imported example packages
    dirs = tuple(d.name for d in packages_dir.iterdir())
    for n in filter(lambda m: m.startswith(dirs), list(sys.modules)):
        # Remove the example.* and example2.*, etc. modules from sys.modules
        # to ensure a clean state for each test
        del sys.modules[n]

    importlib.invalidate_caches()
