from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

from ordeq_viz.api import viz


def test_viz_main_mermaid(tmp_path: Path) -> None:
    output_file = tmp_path / "output.mermaid"
    viz("example", fmt="mermaid", output=output_file)
    assert output_file.exists()
    output_file_content = output_file.read_text("utf8")
    assert "graph TB" in output_file_content


def test_viz_main_mermaid_multiple_packages(tmp_path: Path) -> None:
    output_file = tmp_path / "output.mermaid"
    viz("example", "example2", fmt="mermaid", output=output_file)
    assert output_file.exists()
    output_file_content = output_file.read_text("utf8")
    assert "graph TB" in output_file_content
    assert "transform_input(" in output_file_content
    assert "transform_input_2(" in output_file_content


def test_viz_main_mermaid_multiple_modules(tmp_path: Path) -> None:
    import example.nodes  # ty: ignore[unresolved-import]
    import example2.nodes  # ty: ignore[unresolved-import]

    output_file = tmp_path / "output.mermaid"
    viz(example.nodes, example2.nodes, fmt="mermaid", output=output_file)
    assert output_file.exists()
    output_file_content = output_file.read_text("utf8")
    assert "graph TB" in output_file_content
    assert "world(" in output_file_content
    assert "transform_input(" not in output_file_content
    assert "transform_input_2(" in output_file_content


def test_viz_main_error_when_mixed_inputs(tmp_path: Path) -> None:
    import example.nodes  # ty: ignore[unresolved-import]

    output_file = tmp_path / "output.mermaid"
    with pytest.raises(TypeError, match="All objects provided must be either"):
        viz("example", example.nodes, fmt="mermaid", output=output_file)


def test_viz_main_kedro(tmp_path: Path) -> None:
    output_folder = tmp_path / "kedro_output"
    viz("example", fmt="kedro", output=output_folder)
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
    patched_pipeline_to_mermaid.assert_called_once_with(
        expected_example_node_objects, expected_example_ios
    )


@patch("ordeq_viz.api.pipeline_to_kedro_viz")
def test_viz_to_kedro_call(
    patched_pipeline_to_kedro: MagicMock,
    tmp_path: Path,
    expected_example_node_objects,
    expected_example_ios,
) -> None:
    output_folder = tmp_path / "kedro_output"
    viz("example", fmt="kedro", output=output_folder)
    patched_pipeline_to_kedro.assert_called_once_with(
        expected_example_node_objects,
        expected_example_ios,
        output_directory=output_folder,
    )


def test_viz_main_mermaid_with_callables(tmp_path: Path) -> None:
    import example.nodes  # ty: ignore[unresolved-import]
    import example2.nodes  # ty: ignore[unresolved-import]

    output_file = tmp_path / "output.mermaid"
    viz(
        example.nodes.world,
        example2.nodes.transform_input_2,
        fmt="mermaid",
        output=output_file,
    )
    assert output_file.exists()
    output_file_content = output_file.read_text("utf8")
    assert "graph TB" in output_file_content
    assert "world(" in output_file_content
    assert "transform_input_2(" in output_file_content
    assert "[(x)]" in output_file_content
    assert "[(y)]" in output_file_content
    assert "[(TestInput2)]" in output_file_content
    assert "[(TestOutput2)]" in output_file_content


def test_viz_main_mermaid_with_callables_dynamic_function(
    tmp_path: Path,
) -> None:
    import example3.nodes  # ty: ignore[unresolved-import]

    output_file = tmp_path / "output.mermaid"
    viz(
        example3.nodes.f1, example3.nodes.f2, fmt="mermaid", output=output_file
    )
    assert output_file.exists()
    output_file_content = output_file.read_text("utf8")
    assert "graph TB" in output_file_content
    # we would prefer to see f1 and f2, but since they are dynamically created
    # with the same name, mermaid shows them both as "hello" for now.
    assert (
        """	subgraph pipeline["Pipeline"]
		direction TB
		hello:::function
		hello:::function
	end"""
        in output_file_content
    )


def test_viz_main_mermaid_with_module_dynamic_function(tmp_path: Path) -> None:
    import example3.nodes  # ty: ignore[unresolved-import]

    output_file = tmp_path / "output.mermaid"
    viz(example3.nodes, fmt="mermaid", output=output_file)
    assert output_file.exists()
    output_file_content = output_file.read_text("utf8")
    assert "graph TB" in output_file_content
    # see previous test
    assert (
        """	subgraph pipeline["Pipeline"]
		direction TB
		hello:::function
		hello:::function
	end"""
        in output_file_content
    )
