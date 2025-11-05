from pathlib import Path

from ordeq_files import TextLinesStream


def test_stream_read(tmp_path: Path):
    filepath = tmp_path / "hello.txt"
    filepath.write_text("hello\nworld\n")
    dataset = TextLinesStream(path=filepath)
    assert list(dataset.load()) == ["hello\n", "world\n"]


def test_stream_write(tmp_path: Path):
    filepath = tmp_path / "hello.txt"
    dataset = TextLinesStream(path=filepath)
    dataset.save(line for line in ["hello\n", "world\n"])
    assert filepath.read_text() == "hello\nworld\n"


def test_stream_write_read_multiple_times(tmp_path: Path):
    filepath = tmp_path / "hello.txt"
    dataset = TextLinesStream(path=filepath)
    dataset.save(line for line in ["line1\n", "line2\n", "line3\n"])
    first_read = list(dataset.load())
    second_read = list(dataset.load())
    assert first_read == ["line1\n", "line2\n", "line3\n"]
    assert second_read == ["line1\n", "line2\n", "line3\n"]


def test_log_warning(caplog):
    """
    Make sure that a warning is logged when initializing TextLinesStream
    indicating that it is in pre-release.
    """
    filepath = Path("somefile.txt")
    with caplog.at_level("WARNING"):
        _ = TextLinesStream(path=filepath)
    assert "TextLinesStream is in pre-release" in caplog.text
