from pathlib import Path

from ordeq_files import Bz2


def test_it_loads_and_saves(tmp_path: Path):
    """Test basic save and load functionality."""
    path = tmp_path / "test.bz2"
    data = b"some bytes to compress"
    z = Bz2(path=path)
    z.save(data)
    assert z.load() == data, "Loaded data should match original data"


def test_it_saves_and_loads_with_options(tmp_path: Path):
    """Test save and load with compression options."""
    path = tmp_path / "test_options.bz2"
    data = b"some other bytes to compress with a specific level"
    z = Bz2(path=path)
    # Use a specific compression level
    z.save(data, compresslevel=5)
    loaded_data = z.load()
    assert loaded_data == data, (
        "Loaded data should match original data when saved with options"
    )


def test_load_empty_file(tmp_path: Path):
    """Test loading from an empty compressed file."""
    path = tmp_path / "empty.bz2"
    z = Bz2(path=path)
    # Create an empty compressed file
    z.save(b"")
    assert z.load() == b"", (
        "Loading an empty file should result in empty bytes"
    )


def test_save_and_load_large_file(tmp_path: Path):
    """Test with a larger amount of data."""
    path = tmp_path / "large.bz2"
    # Create a larger data block (e.g., 1MB)
    data = b"A" * (1024 * 1024)
    z = Bz2(path=path)
    z.save(data)
    assert z.load() == data, (
        "Loaded large data should match original large data"
    )
