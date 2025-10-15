import pytest
from ordeq_common import StringBuffer


@pytest.fixture(autouse=True)
def doctest_setup(doctest_namespace):
    """Mock the example datasets that are used in the doctests."""
    doctest_namespace["CSV"] = StringBuffer()
    doctest_namespace["Table"] = StringBuffer()
