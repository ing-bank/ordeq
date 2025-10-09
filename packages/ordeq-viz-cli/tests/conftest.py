import sys
from pathlib import Path

import pytest
from ordeq._registry import NODE_REGISTRY


@pytest.fixture
def resources_dir() -> Path:
    """Return the path to the resources directory.

    Returns:
        the path to the resources directory
    """

    PACKAGE_DIR = Path(__file__).resolve().parent
    return PACKAGE_DIR / "resources"


@pytest.fixture(autouse=True)
def append_resources_dir_to_sys_path(resources_dir):
    """Append the resources directory to sys.path."""
    sys.path.append(str(resources_dir))
    yield
    sys.path.remove(str(resources_dir))
    for n in filter(lambda m: m.startswith("example"), list(sys.modules)):
        # Remove the example.* and example2.* modules from sys.modules
        # to ensure a clean state for each test
        del sys.modules[n]
    NODE_REGISTRY._data.clear()
