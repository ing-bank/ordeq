import sys

from ordeq_common import Print


def test_it_saves(capsys):
    Print().save("Hello, world!")
    captured = capsys.readouterr()
    assert "Hello, world!" in captured.out
    assert not captured.err


def test_it_saves_stderr(capsys):
    Print().save("Hello, world!", file=sys.stderr)
    captured = capsys.readouterr()
    assert not captured.out
    assert "Hello, world!" in captured.err
