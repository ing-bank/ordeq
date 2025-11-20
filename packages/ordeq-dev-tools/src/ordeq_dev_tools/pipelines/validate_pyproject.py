"""Validate the pyproject.toml files of all packages in the monorepo."""

import logging
from pathlib import Path

from ordeq import node
from ordeq_dev_tools.paths import ROOT_PATH, PACKAGES_PATH
from ordeq_dev_tools.pipelines.shared import packages
from ordeq_files import TextLinesStream
from ordeq_toml import TOML

logger = logging.getLogger(__name__)

package_overview = TextLinesStream(path=ROOT_PATH / "docs" / "packages.md")


def get_pypi_name_description_group_logo(
    pyproject_path: Path,
) -> tuple[str, str, str | None, str | None]:
    """Extract the relevant attributes for the package pyproject.tomls, including logo_url from [tool.ordeq-dev].

    Args:
        pyproject_path: The path to the pyproject.toml file.

    Returns:
        A tuple containing the package name, description, group (or None), and logo_url (or None).
    """
    data = TOML(path=pyproject_path).load()
    name = data["project"]["name"]
    description = data["project"].get("description", "")
    tool_section = data.get("tool", {})
    ordeq_dev_section = tool_section.get("ordeq-dev", {})
    logo_url = ordeq_dev_section.get("logo_url", None)
    group = ordeq_dev_section.get("group", None)
    return name, description, group, logo_url


@node(inputs=packages)
def groups(packages: list[str]) -> None:
    """Generate HTML table row data for each package directory, including logo
    (if present).

    Args:
        packages: A list of package directory paths.

    Returns:
        A mapping group names to lists of package dicts.
    """
    error = False

    root_pyproject = TOML(path=ROOT_PATH / "pyproject.toml").load()
    root_tool_section = root_pyproject.get("tool", {})
    uv_section = root_tool_section.get("uv", {})
    sources_section = uv_section.get("sources", {})

    for package in packages:
        pyproject = PACKAGES_PATH / package / "pyproject.toml"
        if not pyproject.exists():
            continue
        pypi_name, description, group, logo_url = get_pypi_name_description_group_logo(
            pyproject
        )

        if package not in sources_section:
            logger.warning(
                f"Warning: Package '{package}' is missing from [tool.uv.sources] in root pyproject.toml."
            )
            error = True

        if not description:
            logger.warning(f"Warning: Package '{package}' is missing a description.")
            error = True
        if not group:
            logger.warning(f"Warning: Package '{package}' is missing a group.")
            error = True
        if not logo_url and group == "io":
            logger.warning(f"Warning: Package '{package}' is missing a logo_url.")
            error = True

    if error:
        raise ValueError(
            "One or more packages are missing required fields in pyproject.toml"
        )
