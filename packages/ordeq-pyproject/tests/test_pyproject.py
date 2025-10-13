from pathlib import Path

import pytest
from ordeq import IOException
from ordeq_pyproject import Pyproject


@pytest.mark.parametrize(
    ("toml_content", "section", "expected"),
    [
        (
            """
[tool.my_tool]
foo = "bar"

[tool.other]
baz = 42
""",
            "tool.my_tool",
            {"foo": "bar"},
        ),
        (
            """
[tool.a]
x = 1
[tool.b]
y = 2
""",
            "tool.b",
            {"y": 2},
        ),
        (
            """
[project]
name = "ordeq"
version = "0.1.0"
""",
            "project",
            {"name": "ordeq", "version": "0.1.0"},
        ),
        (
            """
[tool.my_tool.hello]
foo = "bar"
[tool.my_tool.world]
baz = 42
""",
            "tool.my_tool.hello",
            {"foo": "bar"},
        ),
        (
            """
[tool.my_tool.hello]
foo = "bar"
[tool.my_tool.world]
baz = 42
""",
            "tool.my_tool.hello.foo",
            "bar",
        ),
    ],
)
def test_pyproject_load_section(
    tmp_path: Path, toml_content, section, expected
):
    pyproject_path = tmp_path / "pyproject.toml"
    pyproject_path.write_text(toml_content)
    pyproject = Pyproject(path=pyproject_path, section=section)
    assert pyproject.load() == expected


def test_pyproject_section_missing(tmp_path: Path):
    pyproject_path = tmp_path / "pyproject.toml"
    pyproject_path.write_text("[tool.foo]\na = 1\n")
    pyproject = Pyproject(path=pyproject_path, section="tool.bar")
    with pytest.raises(IOException):
        pyproject.load()
