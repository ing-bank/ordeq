from collections.abc import Callable
from pathlib import Path

import pytest
from ordeq import Node
from ordeq._nodes import get_node
from ordeq._resolve import Catalog
from ordeq_test_utils import append_packages_dir_to_sys_path


@pytest.fixture
def expected_example_nodes() -> set[Callable]:
    """Expected nodes in the example package.

    Returns:
        a set of expected nodes
    """
    from example_1.nodes import world
    from example_1.pipeline import (
        transform_input,
        transform_mock_input,
    )
    from example_1.wrapped_io import (
        hello,
        print_message,
    )

    """Expected nodes in the example package."""
    return {transform_input, transform_mock_input, world, hello, print_message}


@pytest.fixture
def expected_example_ios() -> Catalog:
    """Expected IOs in the example package.

    Returns:
        a dict of expected IOs with their variable name as key
    """
    from example_1.catalog import (
        Hello,
        TestInput,
        TestOutput,
        World,
    )
    from example_1.nodes import x, y
    from example_1.wrapped_io import (
        message,
        name_generator,
        name_printer,
    )

    return {
        ("example_1.catalog", "Hello"): Hello,
        ("example_1.catalog", "TestInput"): TestInput,
        ("example_1.catalog", "TestOutput"): TestOutput,
        ("example_1.catalog", "World"): World,
        ("example_1.nodes", "x"): x,
        ("example_1.nodes", "y"): y,
        ("example_1.pipeline", "Hello"): Hello,
        ("example_1.pipeline", "TestInput"): TestInput,
        ("example_1.pipeline", "TestOutput"): TestOutput,
        ("example_1.pipeline", "World"): World,
        ("example_1.wrapped_io", "message"): message,
        ("example_1.wrapped_io", "name_generator"): name_generator,
        ("example_1.wrapped_io", "name_printer"): name_printer,
    }


@pytest.fixture
def expected_example_node_objects(expected_example_nodes) -> set[Node]:
    """Expected node objects in the example package.

    Returns:
        a set of expected node objects
    """
    return {get_node(f) for f in expected_example_nodes}
