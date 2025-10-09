import sys
from pathlib import Path
from unittest.mock import patch

import pytest
from ordeq_cli_runner import main, parse_args

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
            ("run", "domain_X:name_X", "--hooks", "x:Logger", "y:Debugger"),
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
    ("runnables", "hooks", "expected"),
    [
        pytest.param(["subpackage"], [], "Hello, World!", id="package"),
        pytest.param(
            ["subpackage"],
            ["subpackage.hooks:MyNodeHook"],
            "(before-node)\nHello, World!\n(after-node)",
            id="package + hook",
        ),
        pytest.param(
            ["subpackage"],
            ["subpackage.hooks:MyNodeHook", "subpackage.hooks:MyRunHook"],
            "(before-run)\n"
            "(before-node)\n"
            "Hello, World!\n"
            "(after-node)\n"
            "(after-run)",
            id="package + hooks",
        ),
        pytest.param(["subpackage.hello"], [], "Hello, World!", id="module"),
        pytest.param(
            ["subpackage.hello:world"], [], "Hello, World!", id="node"
        ),
        pytest.param(
            ["subpackage.hello:world"],
            ["subpackage.hooks:MyNodeHook"],
            "(before-node)\nHello, World!\n(after-node)",
            id="node + hook",
        ),
        pytest.param(
            ["subpackage.hello:world"],
            ["subpackage.hooks:MyNodeHook", "subpackage.hooks:MyRunHook"],
            "(before-run)\n"
            "(before-node)\n"
            "Hello, World!\n"
            "(after-node)\n"
            "(after-run)",
            id="node + hooks",
        ),
    ],
)
def test_it_runs(
    capsys: pytest.CaptureFixture,
    runnables: list[str],
    hooks: list[str],
    expected: str,
):
    try:
        sys.path.append(str(RESOURCES_DIR))
        with patch.object(
            sys, "argv", ["ordeq", "run", *runnables, "--hooks", *hooks]
        ):
            main()
            captured = capsys.readouterr()
            assert captured.out.strip() == expected
    finally:
        sys.path.remove(str(RESOURCES_DIR))
