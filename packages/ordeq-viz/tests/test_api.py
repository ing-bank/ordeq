from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

from ordeq_viz.api import viz


def test_viz_main_kedro(tmp_path: Path) -> None:
    output_folder = tmp_path / "kedro_output"
    viz("example", fmt="kedro-viz", output=output_folder)
    assert output_folder.exists()
    assert (output_folder / "api" / "main").exists()


@patch("ordeq_viz.api.pipeline_to_mermaid", return_value="mermaid content")
def test_viz_to_mermaid_call(
    patched_pipeline_to_mermaid: MagicMock,
    tmp_path: Path,
    expected_example_node_objects,
    expected_example_ios,
) -> None:
    output_file = tmp_path / "output.mermaid"
    viz("example", fmt="mermaid", output=output_file)
    patched_pipeline_to_mermaid.assert_called_once()
    actual_node_objs, actual_ios = patched_pipeline_to_mermaid.call_args[0]
    assert actual_node_objs == expected_example_node_objects
    # Two IOs are inlined and thus not included in the actual_ios
    assert all(io in actual_ios for io in expected_example_ios)


@patch("ordeq_viz.api.pipeline_to_kedro_viz")
def test_viz_to_kedro_call(
    patched_pipeline_to_kedro: MagicMock,
    tmp_path: Path,
    expected_example_node_objects,
    expected_example_ios,
) -> None:
    output_folder = tmp_path / "kedro_output"
    viz("example", fmt="kedro-viz", output=output_folder)
    patched_pipeline_to_kedro.assert_called_once()
    actual_node_objs, actual_ios = patched_pipeline_to_kedro.call_args[0]
    actual_kwargs = patched_pipeline_to_kedro.call_args[1]
    assert actual_node_objs == expected_example_node_objects
    assert set(actual_ios) == set(expected_example_ios)
    assert actual_kwargs.get("output_directory") == output_folder


def test_viz_main_kedro_no_output_raises(tmp_path: Path) -> None:
    with pytest.raises(
        ValueError, match="`output` is required when `fmt` is 'kedro-viz'"
    ):
        viz("example", fmt="kedro-viz")
