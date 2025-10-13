"""Generate a markdown table overview of all packages in the packages/
directory.

Each row contains:
- Package name
- PyPI badge+link
- API docs link
- Package description

The resulting markdown is written to docs/packages.md.
"""

import sys
from pathlib import Path

if sys.version_info >= (3, 11):
    import tomllib
else:
    import tomli as tomllib  # ty: ignore[unresolved-import]


def get_package_dirs(packages_dir: Path) -> list[Path]:
    """Return a list of package directories in the given packages_dir.

    Args:
        packages_dir: The path to the directory containing package directories.

    Returns:
        A list of package directory paths.
    """
    return [
        d
        for d in packages_dir.iterdir()
        if d.is_dir() and not d.name.startswith(".")
    ]


def get_pypi_name_and_description(pyproject_path: Path) -> tuple[str, str]:
    """Extract the canonical name and description from a pyproject.toml file.

    Args:
        pyproject_path: The path to the pyproject.toml file.

    Returns:
        A tuple containing the package name and description.
    """
    with pyproject_path.open("rb") as f:
        data = tomllib.load(f)
    name = data["project"]["name"]
    description = data["project"].get("description", "")
    return name, description


def get_pypi_name_description_group(
    pyproject_path: Path,
) -> tuple[str, str, str | None]:
    """Extract the relevant attributes for the package pyproject.tomls.

    Args:
        pyproject_path: The path to the pyproject.toml file.

    Returns:
        A tuple containing the package name, description, and group (or None).
    """
    with pyproject_path.open("rb") as f:
        data = tomllib.load(f)
    name = data["project"]["name"]
    description = data["project"].get("description", "")
    group = None
    tool_section = data.get("tool", {})
    ordeq_section = tool_section.get("ordeq", {})
    if isinstance(ordeq_section, dict):
        group = ordeq_section.get("group")
    return name, description, group


def generate_table_rows_by_group(
    package_dirs: list[Path],
) -> dict[str, list[str]]:
    """Generate markdown table rows for each package directory.

    Args:
        package_dirs: A list of package directory paths.

    Returns:
        A mapping group names to lists of markdown table row strings.
    """
    groups: dict[str, list[str]] = {}
    for pkg_dir in sorted(package_dirs, key=lambda d: d.name):
        pyproject = pkg_dir / "pyproject.toml"
        if not pyproject.exists():
            continue
        pypi_name, description, group = get_pypi_name_description_group(
            pyproject
        )
        name_col = (
            f"[![PyPI](https://img.shields.io/pypi/v/{pypi_name}?label={pkg_dir.name})]"
            f"(https://pypi.org/project/{pypi_name}/)"
        )
        src_name = pkg_dir.name.replace("-", "_")
        docs = f"[API Docs](https://ing-bank.github.io/ordeq/api/{src_name}/)"
        row = f"| {name_col} | {description} | {docs} |"
        group_key = group or "Other"
        groups.setdefault(group_key, []).append(row)
    return groups


def write_markdown_table(rows: list[str], output_path: Path) -> None:
    """Write the markdown table to the given output_path.

    Args:
        rows: A list of markdown table row strings.
        output_path: The path to the output markdown file.
    """
    header = (
        "# Package Overview\n\n"
        "This page lists all packages in the `ordeq` project, with links to "
        "their PyPI pages and API documentation.\n\n"
        "| Name | Description | API Docs |\n"
        "|------|-------------|----------|\n"
    )
    with output_path.open("w", encoding="utf-8") as f:
        f.write(header)
        for row in rows:
            f.write(row + "\n")


def write_markdown_table_by_group(
    groups: dict[str, list[str]], output_path: Path
) -> None:
    """Write the grouped markdown tables to the given output_path.

    Args:
        groups: A dictionary mapping group names to lists of markdown table row
            strings.
        output_path: The path to the output markdown file.
    """
    header = (
        "# Package overview\n\n"
        "This page lists all public packages in the `ordeq` project.\n\n"
    )
    table_header = (
        "| Name | Description | API Docs |\n"
        "|------|-------------|----------|\n"
    )
    group_order = ["framework", "CLI", "ios"]
    excluded_groups = {"developer-tools"}
    pretty_names = {
        "framework": "Framework packages",
        "CLI": "Command line interfaces",
        "ios": "IO packages",
        "Other": "Other packages",
    }
    group_descriptions = {
        "framework": "Libraries that provide framework functionality "
        "for Ordeq.",
        "CLI": "Command line tools for interacting with Ordeq.",
        "ios": "Packages that provide implementations of inputs and outputs.",
        "Other": "Packages not assigned to a specific group.",
    }
    with output_path.open("w", encoding="utf-8") as f:
        f.write(header)
        # Write groups in the specified order first
        for group in group_order:
            if group in groups and group not in excluded_groups:
                pretty = pretty_names.get(group, group)
                desc = group_descriptions.get(group, "")
                f.write(f"## {pretty}\n\n")
                if desc:
                    f.write(f"{desc}\n\n")
                f.write(table_header)
                for row in groups[group]:
                    f.write(row + "\n")
                f.write("\n")
        # Write any other groups (except excluded)
        for group in sorted(groups):
            if group in group_order or group in excluded_groups:
                continue
            pretty = pretty_names.get(group, group)
            desc = group_descriptions.get(group, "")
            f.write(f"## {pretty}\n\n")
            if desc:
                f.write(f"{desc}\n\n")
            f.write(table_header)
            for row in groups[group]:
                f.write(row + "\n")
            f.write("\n")


if __name__ == "__main__":
    """Generate the package overview markdown file."""
    print("Generating package overview...")
    root = Path(__file__).parent.parent
    packages_dir = root / "packages"
    output_path = root / "docs" / "packages.md"
    package_dirs = get_package_dirs(packages_dir)
    groups = generate_table_rows_by_group(package_dirs)
    write_markdown_table_by_group(groups, output_path)
