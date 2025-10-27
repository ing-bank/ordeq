# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "ordeq-toml",
# ]
# ///
"""Generate a markdown table overview of all packages in the packages/
directory. The resulting markdown is written to docs/packages.md.
"""

from pathlib import Path

from ordeq_toml import TOML


def get_package_dirs(packages_dir: Path) -> list[Path]:
    """Return a list of package directories in the given packages_dir.

    Args:
        packages_dir: The path to the directory containing package directories.

    Returns:
        A list of package directory paths.
    """
    return [d for d in packages_dir.iterdir() if d.is_dir()]


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


def write_html_table_by_group(
    groups: dict[str, list[dict]], output_path: Path
) -> None:
    """Write the grouped HTML tables to the given output_path, with logo column and proper sizing.

    Args:
        groups: A dictionary mapping group names to lists of package dicts.
        output_path: The path to the output markdown file.
    """
    header = (
        "# Package overview\n\n"
        "This page lists all public packages in the `ordeq` project.\n\n"
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
        "framework": "Libraries that provide framework functionality for Ordeq.",
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
                f.write(
                    "<table>\n  <tr>\n    <th width='90' style='text-align:center;vertical-align:middle;max-height:35px;'></th>\n    <th style='text-align:left;vertical-align:middle;max-height:35px;'>Name</th>\n    <th style='text-align:left;vertical-align:middle;max-height:35px;'>Description</th>\n    <th style='text-align:left;vertical-align:middle;max-height:35px;'>API Docs</th>\n  </tr>\n"
                )
                for pkg in groups[group]:
                    logo_html = (
                        f"<img src='{pkg['logo_url']}' alt='logo' style='max-height:35px;'/>"
                        if pkg["logo_url"]
                        else ""
                    )
                    name_html = (
                        f"<a href='https://pypi.org/project/{pkg['pypi_name']}/'>"
                        f"<img src='https://img.shields.io/pypi/v/{pkg['pypi_name']}?label={pkg['pkg_dir']}' style='max-height:35px;'/></a>"
                    )
                    docs_html = f"<a href='https://ing-bank.github.io/ordeq/api/{pkg['src_name']}/'>API Docs</a>"
                    f.write(
                        f"  <tr>\n    <td align='center' width='90' style='text-align:center;vertical-align:middle;max-height:35px;'>{logo_html}</td>\n    <td align='left' style='text-align:left;vertical-align:middle;max-height:35px;'>{name_html}</td>\n    <td align='left' style='text-align:left;vertical-align:middle;max-height:35px;'>{pkg['description']}</td>\n    <td align='left' style='text-align:left;vertical-align:middle;max-height:35px;'>{docs_html}</td>\n  </tr>\n"
                    )
                f.write("</table>\n\n")
        # Write any other groups (except excluded)
        for group in sorted(groups):
            if group in group_order or group in excluded_groups:
                continue
            pretty = pretty_names.get(group, group)
            desc = group_descriptions.get(group, "")
            f.write(f"## {pretty}\n\n")
            if desc:
                f.write(f"{desc}\n\n")
            f.write(
                "<table>\n  <tr>\n    <th width='90' style='text-align:center;vertical-align:middle;max-height:35px;'></th>\n    <th style='text-align:left;vertical-align:middle;max-height:35px;'>Name</th>\n    <th style='text-align:left;vertical-align:middle;max-height:35px;'>Description</th>\n    <th style='text-align:left;vertical-align:middle;max-height:35px;'>API Docs</th>\n  </tr>\n"
            )
            for pkg in groups[group]:
                logo_html = (
                    f"<img src='{pkg['logo_url']}' alt='logo' style='max-height:35px;'/>"
                    if pkg["logo_url"]
                    else ""
                )
                name_html = (
                    f"<a href='https://pypi.org/project/{pkg['pypi_name']}/'>"
                    f"<img src='https://img.shields.io/pypi/v/{pkg['pypi_name']}?label={pkg['pkg_dir']}' style='max-height:35px;'/></a>"
                )
                docs_html = f"<a href='https://ing-bank.github.io/ordeq/api/{pkg['src_name']}/'>API Docs</a>"
                f.write(
                    f"  <tr>\n    <td align='center' width='90' style='text-align:center;vertical-align:middle;max-height:35px;'>{logo_html}</td>\n    <td align='left' style='text-align:left;vertical-align:middle;max-height:35px;'>{name_html}</td>\n    <td align='left' style='text-align:left;vertical-align:middle;max-height:35px;'>{pkg['description']}</td>\n    <td align='left' style='text-align:left;vertical-align:middle;max-height:35px;'>{docs_html}</td>\n  </tr>\n"
                )
            f.write("</table>\n\n")


def generate_html_table_rows_by_group(
    package_dirs: list[Path],
) -> dict[str, list[dict]]:
    """Generate HTML table row data for each package directory, including logo
    (if present).

    Args:
        package_dirs: A list of package directory paths.

    Returns:
        A mapping group names to lists of package dicts.
    """
    groups: dict[str, list[dict]] = {}
    for pkg_dir in sorted(package_dirs, key=lambda d: d.name):
        pyproject = pkg_dir / "pyproject.toml"
        if not pyproject.exists():
            continue
        pypi_name, description, group, logo_url = (
            get_pypi_name_description_group_logo(pyproject)
        )
        src_name = pkg_dir.name.replace("-", "_")
        pkg_data = {
            "logo_url": logo_url,
            "pypi_name": pypi_name,
            "description": description,
            "pkg_dir": pkg_dir.name,
            "src_name": src_name,
        }
        group_key = group or "Other"
        groups.setdefault(group_key, []).append(pkg_data)
    return groups


if __name__ == "__main__":
    """Generate the package overview markdown file."""
    print("Generating package overview...")
    root = Path(__file__).parent.parent
    packages_dir = root / "packages"
    output_path = root / "docs" / "packages.md"
    package_dirs = get_package_dirs(packages_dir)
    groups = generate_html_table_rows_by_group(package_dirs)
    write_html_table_by_group(groups, output_path)
