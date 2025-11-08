import sys
from pathlib import Path
from unittest.mock import patch

from ordeq_viz_cli import main


def test_runs_viz(tmp_path: Path):
    output_file = tmp_path / "output.mermaid"
    with patch.object(
        sys,
        "argv",
        [
            "ordeq-viz",
            "--package",
            "example",
            "--fmt",
            "mermaid",
            "--output",
            str(output_file),
        ],
    ):
        main()
    assert output_file.exists()
    output_file_content = output_file.read_text("utf8")
    assert "graph TB" in output_file_content
    assert "transform_input_2" in output_file_content


def test_runs_viz_with_options(tmp_path: Path):
    output_file = tmp_path / "output.mermaid"
    with patch.object(
        sys,
        "argv",
        [
            "ordeq-viz",
            "--package",
            "example",
            "--fmt",
            "mermaid-md",
            "--output",
            str(output_file),
            "--option",
            "block_char",
            ":",
        ],
    ):
        main()
    assert output_file.exists()
    output_file_content = output_file.read_text("utf8")
    assert "graph TB" in output_file_content
    assert "transform_input_2" in output_file_content
    assert ":::mermaid" in output_file_content
