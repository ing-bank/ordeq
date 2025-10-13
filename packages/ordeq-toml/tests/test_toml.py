import math
from pathlib import Path

import pytest
from ordeq_toml import TOML


@pytest.mark.parametrize(
    "data",
    [
        {},
        {"a": 1, "b": "foo"},
        {"section": {"x": 42, "y": [1, 2, 3]}},
        {"list": [1, 2, 3], "bool": True, "float": math.pi},
    ],
)
def test_toml_io(tmp_path: Path, data) -> None:
    toml_path = tmp_path / "test.toml"
    io = TOML(path=toml_path)
    io.save(data)
    assert toml_path.exists()
    loaded = io.load()
    assert loaded == data


@pytest.mark.parametrize(
    ("content", "expected"),
    [
        ("# This is a comment\nfoo = 'bar'\n", {"foo": "bar"}),
        ("foo = 'bar' # Inline comment\n", {"foo": "bar"}),
        ("# Only a comment\n", {}),
        ("foo = 1\n# trailing comment\nbar = 2\n", {"foo": 1, "bar": 2}),
    ],
)
def test_toml_comments(tmp_path: Path, content, expected) -> None:
    toml_path = tmp_path / "comments.toml"
    with toml_path.open("w", encoding="utf-8") as f:
        f.write(content)
    io = TOML(path=toml_path)
    loaded = io.load()
    assert loaded == expected
