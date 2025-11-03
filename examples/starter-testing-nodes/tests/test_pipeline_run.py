from pathlib import Path

from ordeq import run
from ordeq_files import CSV
from starter_testing_nodes.catalog import greetings, names
from starter_testing_nodes.pipeline import greet


def test_run_greet():
    TEST_RESOURCES_DIR = (
        Path(__file__).resolve().parent.parent / "tests-resources"
    )
    test_names = CSV(path=TEST_RESOURCES_DIR / "test-names.csv")
    test_greetings = CSV(path=TEST_RESOURCES_DIR / "test-greetings.csv")
    run(greet, io={names: test_names, greetings: test_greetings})
    assert test_greetings.load() == [
        ["Hello, Alexis!"],
        ["Hello, Alice!"],
        ["Hello, Marco!"],
        ["Hello, Julian!"],
        ["Hello, Daisy!"],
        ["Hello, Philippe!"],
    ]


import starter_testing_nodes  # noqa: E402 (import-not-at-top)
import test_catalog  # noqa: E402 (import-not-at-top)


def test_run_greet_catalog():
    run(greet, io={starter_testing_nodes.catalog: test_catalog})
    assert test_catalog.greetings.load() == [
        ["Hello, Alexis!"],
        ["Hello, Alice!"],
        ["Hello, Marco!"],
        ["Hello, Julian!"],
        ["Hello, Daisy!"],
        ["Hello, Philippe!"],
    ]
