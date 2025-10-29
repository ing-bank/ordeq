from pathlib import Path

import pytest
from ordeq_test_utils import append_packages_dir_to_sys_path


@pytest.fixture
def packages_dir() -> Path:
    """Return the path to the packages directory.

    Returns:
        the path to the packages directory
    """

    PACKAGE_DIR = Path(__file__).resolve().parents[2] / "ordeq" / "tests"
    return PACKAGE_DIR / "packages"


@pytest.fixture(autouse=True)
def packages(packages_dir):
    """Append the packages directory to sys.path."""
    yield from append_packages_dir_to_sys_path(packages_dir)
