from ordeq import node
from ordeq_dev_tools.paths import PACKAGES_PATH


@node
def packages() -> list[str]:
    """Gets a list of package names from the packages directory.

    Returns:
        Package names
    """
    return sorted([d.name for d in PACKAGES_PATH.iterdir() if d.is_dir()])
