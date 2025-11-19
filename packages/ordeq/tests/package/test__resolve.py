from collections.abc import Callable

import pytest
from ordeq import Node, node
from ordeq._nodes import get_node
from ordeq._resolve import (
    _is_node,
    _resolve_object_ref_to_node,
    _resolve_runnables_to_nodes,
)


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
    return {get_node(f) for f in expected_example_nodes}


def test_gather_nodes_from_module():
    from example_1 import nodes as mod

    assert get_node(mod.world) is not None


def test_resolve_node_by_reference(expected_example_node_objects) -> None:
    """Test resolving nodes by reference."""
    from example_1.nodes import world  # ty: ignore[unresolved-import]

    nodes = _resolve_runnables_to_nodes("example_1.nodes:world")
    assert nodes == [(("example_1.nodes", "world"), get_node(world))]


def test_resolve_node_by_reference_not_a_node() -> None:
    """Test resolving nodes by reference when the reference is not a node."""

    with pytest.raises(
        ValueError,
        match=r"Node 'i_do_not_exist' not found "
        r"in module 'example_1.nodes'",
    ):
        _resolve_runnables_to_nodes("example_1.nodes:i_do_not_exist")


def test_resolve_node_by_reference_no_module() -> None:
    with pytest.raises(
        ValueError, match="Invalid object reference: 'invalidformat'"
    ):
        _resolve_object_ref_to_node("invalidformat")


def test_is_node_proxy():
    def func():
        pass

    proxy = node(func)
    assert _is_node(proxy)
    assert not _is_node(func)
    assert not _is_node(object)
    assert not _is_node(None)

    # Object with fake __ordeq_node__ attribute (not a Node)
    class Fake:
        def __call__(self):
            pass

    fake_obj = Fake()
    fake_obj.__ordeq_node__ = "not_a_node"
    assert not _is_node(fake_obj)

    # Object with __ordeq_node__ attribute that is a Node, but not callable
    class NotCallable:
        __ordeq_node__ = proxy

    not_callable = NotCallable()
    assert not _is_node(not_callable)
