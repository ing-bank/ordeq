from collections.abc import Callable

import pytest
from ordeq import node
from ordeq._fqn import FQN
from ordeq._nodes import get_node
from ordeq._resolve import (
    Pipeline,
    _is_node,
    _resolve_node_reference,
    _resolve_runnables_to_nodes,
)


@pytest.fixture
def expected_example_nodes(packages) -> dict[FQN, Callable]:
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
    return {
        ("example.pipeline", "transform_input"): transform_input,
        ("example.pipeline", "transform_mock_input"): transform_mock_input,
        ("example.nodes", "world"): world,
        ("example.wrapped_io", "hello"): hello,
        ("example.wrapped_io", "print_message"): print_message,
    }


@pytest.fixture
def expected_example_node_objects(expected_example_nodes) -> Pipeline:
    """Expected node objects in the example package.

    Returns:
        a set of expected node objects
    """
    return {key: get_node(f) for key, f in expected_example_nodes.items()}


def test_gather_nodes_from_module(packages):
    from example import nodes as mod  # ty: ignore[unresolved-import]

    assert get_node(mod.world) is not None


def test_resolve_node_by_reference(
    expected_example_node_objects, packages
) -> None:
    """Test resolving nodes by reference."""
    from example.nodes import world  # ty: ignore[unresolved-import]

    nodes = _resolve_runnables_to_nodes("example.nodes:world")
    assert nodes == {("example.nodes", "world"): get_node(world)}


def test_resolve_node_by_reference_not_a_node(packages) -> None:
    """Test resolving nodes by reference when the reference is not a node."""

    with pytest.raises(
        ValueError,
        match=r"Node 'i_do_not_exist' not found in module 'example.nodes'",
    ):
        _resolve_runnables_to_nodes("example.nodes:i_do_not_exist")


def test_resolve_node_by_reference_no_module() -> None:
    with pytest.raises(
        ValueError, match="Invalid object reference: 'invalidformat'"
    ):
        _resolve_node_reference("invalidformat")


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
