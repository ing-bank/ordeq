from pathlib import Path

import pandas as pd
import pytest


@pytest.fixture
def resources_dir(request: pytest.FixtureRequest) -> Path:
    """Loads a `Path` referring to the resources directory specific to the
    requesting test module.

    For example, in tests/test_sth.py, this test should pass:

    >>> def test_method(resources_dir):
    ...     assert resources_dir == "tests/test_sth"

    Can be used to load and save data during tests in its own dedicated
    folder, for instance:

    >>> def test_method(resources_dir):
    ...     with open(resources_dir / "test_method.csv", "r") as file:
    ...         assert len(file.readlines()) == 1

    Args:
        request: the `FixtureRequest` of the requesting test module

    Returns:
        the path to the resources directory
    """

    (test_file_dot_py, _, _) = request.node.location
    test_file = Path(*Path(test_file_dot_py).with_suffix("").parts[3:])
    return Path(__file__).parent / "tests-resources" / test_file


@pytest.fixture
def pdf() -> pd.DataFrame:
    return pd.DataFrame(
        data=[(1, "Netherlands"), (2, "Belgium"), (3, "Germany")],
        columns=["key", "value"],
    )
