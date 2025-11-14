from pathlib import Path

from ordeq_files import Gzip


def test_it_loads_and_saves(tmp_path: Path):
    """Test basic save and load functionality."""
    path = tmp_path / "test.gz"
    data = b"some bytes to compress"
    gz = Gzip(path=path)
    gz.save(data)
    assert gz.load() == data, "Loaded data should match original data"


def test_it_saves_and_loads_with_options(tmp_path: Path):
    """Test save and load with compression options."""
    path = tmp_path / "test_options.gz"
    data = b"some other bytes to compress with a specific level"
    gz = Gzip(path=path)
    # Use a specific compression level
    gz.save(data, compresslevel=5)
    loaded_data = gz.load()
    assert loaded_data == data, (
        "Loaded data should match original data when saved with options"
    )


def test_load_empty_file(tmp_path: Path):
    """Test loading from an empty compressed file."""
    path = tmp_path / "empty.gz"
    gz = Gzip(path=path)
    # Create an empty compressed file
    gz.save(b"")
    assert gz.load() == b"", (
        "Loading an empty file should result in empty bytes"
    )


def test_save_and_load_large_file(tmp_path: Path):
    """Test with a larger amount of data."""
    path = tmp_path / "large.gz"
    # Create a larger data block (e.g., 1MB)
    data = b"A" * (1024 * 1024)
    gz = Gzip(path=path)
    gz.save(data)
    assert gz.load() == data, (
        "Loaded large data should match original large data"
    )
