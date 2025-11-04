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
