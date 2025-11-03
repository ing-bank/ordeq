from pathlib import Path

from ordeq_files import FileStream


def test_stream_read(tmp_path: Path):
    filepath = tmp_path / "hello.txt"
    filepath.write_text("hello\nworld\n")
    dataset = FileStream[str](path=filepath)
    assert list(dataset.load()) == ["hello\n", "world\n"]


def test_stream_write(tmp_path: Path):
    filepath = tmp_path / "hello.txt"
    dataset = FileStream[str](path=filepath, mode="w+")
    dataset.save(["hello\n", "world\n"])
    assert filepath.read_text() == "hello\nworld\n"
