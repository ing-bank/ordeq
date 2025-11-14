import os
from pathlib import Path

ROOT_PATH = Path(
    os.environ.get("REPOSITORY_ROOT", Path(__file__).parent.parent.parent.parent.parent)
).resolve()
DATA_PATH = ROOT_PATH / "data" / "dev_tools"
DATA_PATH.mkdir(parents=True, exist_ok=True)
PACKAGES_PATH = ROOT_PATH / "packages"
