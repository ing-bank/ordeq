import subprocess
from pathlib import Path

REPO_ROOT: Path = Path(__file__).resolve().parent.parent


def run_command(command: list[str]) -> str | None:
    """Runs a shell command and returns its output.

    Args:
        command: List of command arguments

    Returns:
        Output of the command as a string
    """
    try:
        result = subprocess.run(
            command, capture_output=True, text=True, check=True, cwd=REPO_ROOT
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError:
        return None
