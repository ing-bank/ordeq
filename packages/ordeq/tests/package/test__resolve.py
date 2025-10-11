from collections.abc import Callable

import pytest
from ordeq import IO, Input, Node, Output
from ordeq._nodes import get_node
from ordeq._resolve import (
    _gather_nodes_from_registry,
    _resolve_module_to_ios,
    _resolve_node_reference,
    _resolve_runnables_to_nodes,
    _resolve_runnables_to_nodes_and_ios,
)
from ordeq_common import StringBuffer


@pytest.fixture
def expected_example_nodes(packages) -> set[Callable]:
    """Expected nodes in the example package.

    Returns:
        a set of expected nodes
    """
    from example.nodes import world  # ty: ignore[unresolved-import]
    from example.pipeline import (  # ty: ignore[unresolved-import]
        transform_input,
        transform_mock_input,
    )
    from example.wrapped_io import (  # ty: ignore[unresolved-import]
        hello,
        print_message,
    )

    """Expected nodes in the example package."""
    return {transform_input, transform_mock_input, world, hello, print_message}


@pytest.fixture
def expected_example_ios(packages) -> dict[str, IO | Input | Output]:
    """Expected IOs in the example package.

    Returns:
        a dict of expected IOs with their variable name as key
    """
    from example.catalog import (  # ty: ignore[unresolved-import]
        Hello,
        TestInput,
        TestOutput,
        World,
    )
    from example.nodes import x, y  # ty: ignore[unresolved-import]
    from example.wrapped_io import (  # ty: ignore[unresolved-import]
        message,
        name_generator,
        name_printer,
    )

    return {
        "Hello": Hello,
        "TestInput": TestInput,
        "TestOutput": TestOutput,
        "World": World,
        "x": x,
        "y": y,
        "message": message,
        "name_generator": name_generator,
        "name_printer": name_printer,
    }


@pytest.fixture
def expected_example_node_objects(expected_example_nodes) -> set[Node]:
    """Expected node objects in the example package.

    Returns:
        a set of expected node objects
    """
    return {get_node(f) for f in expected_example_nodes}


def test_gather_ios_from_module(packages):
    from example import catalog as mod  # ty: ignore[unresolved-import]

    datasets = _resolve_module_to_ios(mod)

    assert len(datasets) == 4
    assert isinstance(datasets["Hello"], StringBuffer)
    assert isinstance(datasets["World"], StringBuffer)
    assert datasets["TestInput"].__class__.__name__ == "MockInput"
    assert datasets["TestOutput"].__class__.__name__ == "MockOutput"


def test_gather_nodes_from_module(packages):
    from example import nodes as mod  # ty: ignore[unresolved-import]

    nodes = _gather_nodes_from_registry()

    assert len(nodes) >= 1
    assert get_node(mod.world) in nodes


def test_gather_nodes_and_ios_from_package(
    expected_example_nodes, expected_example_ios, packages
) -> None:
    """Test gathering nodes and IOs from a package."""
    import example  # ty: ignore[unresolved-import]

    nodes, ios = _resolve_runnables_to_nodes_and_ios(example)
    assert expected_example_nodes == {n.func for n in nodes}
    assert expected_example_ios == ios


def test_resolve_node_by_reference(
    expected_example_node_objects, packages
) -> None:
    """Test resolving nodes by reference."""
    from example.nodes import world  # ty: ignore[unresolved-import]

    nodes = _resolve_runnables_to_nodes("example.nodes:world")
    assert nodes == {get_node(world)}


def test_resolve_node_by_reference_not_a_node(packages) -> None:
    """Test resolving nodes by reference when the reference is not a node."""

    with pytest.raises(
        ValueError,
        match=r"Node 'i_do_not_exist' not found in module 'example.nodes'",
    ):
        _resolve_runnables_to_nodes("example.nodes:i_do_not_exist")


def test_resolve_node_by_reference_no_module() -> None:
    with pytest.raises(
        ValueError, match="Invalid node reference: 'invalidformat'"
    ):
        _resolve_node_reference("invalidformat")
