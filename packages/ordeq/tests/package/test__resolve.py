from collections.abc import Callable

import pytest
from ordeq import Node
from ordeq._resolve import _resolve_runnables_to_nodes


@pytest.fixture
def expected_example_nodes() -> set[Callable]:
    """Expected nodes in the example package.

    Returns:
        a set of expected nodes
    """
    from example_1.nodes import world
    from example_1.pipeline import transform_input, transform_mock_input
    from example_1.wrapped_io import hello, print_message

    """Expected nodes in the example package."""
    return {transform_input, transform_mock_input, world, hello, print_message}


@pytest.fixture
def expected_example_node_objects(expected_example_nodes) -> set[Node]:
    """Expected node objects in the example package.

    Returns:
        a set of expected node objects
    """
    return set(expected_example_nodes)


def test_gather_nodes_from_module():
    from example_1 import nodes as mod

    assert mod.world is not None


def test_resolve_node_by_reference(expected_example_node_objects) -> None:
    """Test resolving nodes by reference."""
    from example_1.nodes import world  # ty: ignore[unresolved-import]

    nodes = _resolve_runnables_to_nodes("example_1.nodes:world")
    assert nodes == [world]


def test_resolve_node_by_reference_not_a_node() -> None:
    """Test resolving nodes by reference when the reference is not a node."""

    with pytest.raises(
        ValueError,
        match=r"Node 'i_do_not_exist' not found "
        r"in module 'example_1.nodes'",
    ):
        _resolve_runnables_to_nodes("example_1.nodes:i_do_not_exist")
