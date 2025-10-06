import importlib
import sys
from pathlib import Path

import pytest
from ordeq.framework._registry import NODE_REGISTRY
from ordeq_common import StringBuffer


@pytest.fixture(autouse=True)
def doctest_setup(doctest_namespace):
    """Mock the example datasets that are used in the doctests."""
    doctest_namespace["CSV"] = StringBuffer()
    doctest_namespace["Table"] = StringBuffer()


@pytest.fixture
def packages_dir() -> Path:
    """Return the path to the example packages directory.

    Returns:
        the path to the packages directory
    """

    PACKAGE_DIR = Path(__file__).resolve().parent.parent
    return PACKAGE_DIR / "packages"


@pytest.fixture
def append_packages_dir_to_sys_path(packages_dir):
    """Append the packages directory to `sys.path`.
    This allows us to import the example packages at test time.
    """

    sys.path.append(str(packages_dir))
    yield
    sys.path.remove(str(packages_dir))

    # Cleanup imported example packages
    dirs = packages_dir.iterdir()
    dirs = [d.name for d in dirs]
    for n in filter(lambda m: m.startswith(tuple(dirs)), list(sys.modules)):
        # Remove the example.* and example2.*, etc. modules from sys.modules
        # to ensure a clean state for each test
        del sys.modules[n]

    NODE_REGISTRY._data.clear()
    importlib.invalidate_caches()
