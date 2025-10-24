from pathlib import Path
from ordeq_test_utils.snapshot import capture_module


def test_it_captures_module(
    caplog, capsys
):
    capture_module(
        Path(__file__).resolve().parent / "expr.py",
                   caplog,
                   capsys)
