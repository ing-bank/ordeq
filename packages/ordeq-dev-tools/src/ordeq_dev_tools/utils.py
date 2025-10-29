import subprocess  # noqa: S404

from ordeq_dev_tools.paths import ROOT_PATH


def run_command(command: list[str]) -> str | None:
    """Runs a shell command and returns its output.

    Args:
        command: List of command arguments

    Returns:
        Output of the command as a string
    """
    try:
        result = subprocess.run(  # noqa: S603
            command, capture_output=True, text=True, check=True, cwd=ROOT_PATH
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError:
        return None
