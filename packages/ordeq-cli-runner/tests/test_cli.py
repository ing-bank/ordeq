from ordeq_cli_runner import main
import sys
from unittest.mock import patch

import pytest
from ordeq_cli_runner import parse_args
from pathlib import Path

RESOURCES_DIR = Path(__file__).parent / "resources"


@pytest.mark.parametrize(
    ("args", "expected"),
    [
        (
                ("run", "domain_A:name_A"),
                {
                    "action": "run",
                    "runnables": ["domain_A:name_A"],
                    "hooks": [],
                    "save": "all",
                },
        ),
        (
                ("run", "domain_A:name_A", "domain_B:name_B"),
                {
                    "action": "run",
                    "runnables": ["domain_A:name_A", "domain_B:name_B"],
                    "hooks": [],
                    "save": "all",
                },
        ),
        (
                ("run", "domain_X:name_X", "--save", "sinks"),
                {
                    "action": "run",
                    "runnables": ["domain_X:name_X"],
                    "hooks": [],
                    "save": "sinks",
                },
        ),
        (
                ("run", "domain_X:name_X", "--hooks", "x:Logger"),
                {
                    "action": "run",
                    "runnables": ["domain_X:name_X"],
                    "hooks": ["x:Logger"],
                    "save": "all",
                },
        ),
        (
                ("run", "domain_X:name_X", "--hooks", "x:Logger",
                 "y:Debugger"),
                {
                    "action": "run",
                    "runnables": ["domain_X:name_X"],
                    "hooks": ["x:Logger", "y:Debugger"],
                    "save": "all",
                },
        ),
    ],
)
def test_it_parses(args, expected):
    assert vars(parse_args(args)) == expected


def test_missing_runnables():
    with pytest.raises(SystemExit):
        parse_args(("run",))


@pytest.mark.parametrize(
    "runnable",
    [
        "subpackage",
        "subpackage.hello",
        "subpackage.hello:world",
    ]
)
def test_it_runs(capsys: pytest.CaptureFixture, runnable: str):
    try:
        sys.path.append(str(RESOURCES_DIR))
        with patch.object(
            sys,
            "argv",
            [
                "ordeq",
                "run",
                runnable,
            ],
        ):
            main()
            captured = capsys.readouterr()
            assert captured.out.strip() == "Hello, World!"
    finally:
        sys.path.remove(str(RESOURCES_DIR))
