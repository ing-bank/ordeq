from pathlib import Path

ROOT_PATH = Path(__file__).resolve().parent.parent.parent.parent.parent
DATA_PATH = ROOT_PATH / "data" / "dev_tools"
DATA_PATH.mkdir(parents=True, exist_ok=True)
PACKAGES_PATH = ROOT_PATH / "packages"
