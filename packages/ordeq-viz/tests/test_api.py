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


def test_viz_main_mixed_inputs(tmp_path: Path) -> None:
    import example.nodes  # ty: ignore[unresolved-import]

    output_file = tmp_path / "output.mermaid"
    viz("example", example.nodes, fmt="mermaid", output=output_file)
    assert output_file.exists()
    output_file_content = output_file.read_text("utf8")
    assert "graph TB" in output_file_content


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
    viz("example", fmt="kedro-viz", output=output_folder)
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
        '\tsubgraph pipeline["Pipeline"]\n'
        "\t\tdirection TB\n"
        "\t\thello([hello]):::node\n"
        "\t\thello([hello]):::node\n"
        "\tend\n" in output_file_content
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
        '\tsubgraph pipeline["Pipeline"]\n'
        "\t\tdirection TB\n"
        "\t\thello([hello]):::node\n"
        "\t\thello([hello]):::node\n"
        "\tend\n" in output_file_content
    )


def test_rag(tmp_path: Path, packages_dir: Path):
    import rag_pipeline  # ty: ignore[unresolved-import]  # noqa: F401,RUF100

    output_file = tmp_path / "output.mermaid"

    viz(
        "rag_pipeline",
        fmt="mermaid",
        output=output_file,
        io_shape_template="({value})",
        use_dataset_styles=True,
        legend=True,
        title="RAG Pipeline",
    )

    content = output_file.read_text()
    expected = (packages_dir / "rag_pipeline.mermaid").read_text()
    assert content == expected


def test_viz_main_kedro_no_output_raises(tmp_path: Path) -> None:
    with pytest.raises(
        ValueError, match="`output` is required when `fmt` is 'kedro-viz'"
    ):
        viz("example", fmt="kedro-viz")


def test_viz_main_mermaid_no_output_returns_str() -> None:
    result = viz("example", fmt="mermaid", output=None)
    assert isinstance(result, str)
    assert "graph TB" in result
