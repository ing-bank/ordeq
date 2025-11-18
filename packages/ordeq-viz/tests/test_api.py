from pathlib import Path

import pytest

from ordeq_viz.api import viz


def test_viz_main_kedro(tmp_path: Path) -> None:
    output_folder = tmp_path / "kedro_output"
    viz("example_1", fmt="kedro-viz", output=output_folder)
    assert output_folder.exists()
    assert (output_folder / "api" / "main").exists()


def test_viz_main_kedro_no_output_raises(tmp_path: Path) -> None:
    with pytest.raises(
        ValueError, match="`output` is required when `fmt` is 'kedro-viz'"
    ):
        viz("example_1", fmt="kedro-viz")
