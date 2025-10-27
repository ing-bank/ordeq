from collections.abc import Callable
from pathlib import Path

import pytest
from ordeq import Node
from ordeq._fqn import FQN
from ordeq._io import AnyIO
from ordeq._nodes import get_node
from ordeq_test_utils import append_packages_dir_to_sys_path


@pytest.fixture
def packages_dir() -> Path:
    """Return the path to the packages directory.

    Returns:
        the path to the packages directory
    """

    PACKAGE_DIR = Path(__file__).resolve().parent
    return PACKAGE_DIR / "packages"


@pytest.fixture(autouse=True)
def packages(packages_dir):
    """Append the packages directory to sys.path."""
    yield from append_packages_dir_to_sys_path(packages_dir)


@pytest.fixture
def expected_example_nodes() -> dict[FQN, Callable]:
    """Expected nodes in the example package.

    Returns:
        a set of expected nodes
    """
    from example.nodes import (  # ty: ignore[unresolved-import]
        node_with_inline_io,
        world,
    )
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
        ("example.nodes", "node_with_inline_io"): node_with_inline_io,
    }


@pytest.fixture
def expected_example_ios() -> dict[FQN, AnyIO]:
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
        ("example.catalog", "Hello"): Hello,
        ("example.catalog", "TestInput"): TestInput,
        ("example.catalog", "TestOutput"): TestOutput,
        ("example.catalog", "World"): World,
        ("example.nodes", "x"): x,
        ("example.nodes", "y"): y,
        ("example.pipeline", "Hello"): Hello,
        ("example.pipeline", "TestInput"): TestInput,
        ("example.pipeline", "TestOutput"): TestOutput,
        ("example.pipeline", "World"): World,
        ("example.wrapped_io", "message"): message,
        ("example.wrapped_io", "name_generator"): name_generator,
        ("example.wrapped_io", "name_printer"): name_printer,
    }


@pytest.fixture
def expected_example_node_objects(expected_example_nodes) -> dict[FQN, Node]:
    """Expected node objects in the example package.

    Returns:
        a set of expected node objects
    """
    return {key: get_node(f) for key, f in expected_example_nodes.items()}
