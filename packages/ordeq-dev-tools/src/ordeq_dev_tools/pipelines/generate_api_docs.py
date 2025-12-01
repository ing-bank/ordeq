"""Generate the content of the 'docs/api/' directory, mirroring the content
of 'packages/*/src'. Creates a Markdown file for each Python module (except
some special ones like __init__). Each Markdown file contains a reference to
the Python module. `mkdocstrings` then picks up the reference and generates
the Markdown file content based on the string docs in the module.

More info: https://mkdocstrings.github.io/ .

Note: there are existing MkDocs plugins available that achieve something
similar, but I find these unnecessary for our use case.
"""

import shutil

from ordeq import node
from ordeq_dev_tools.paths import ROOT_PATH, PACKAGES_PATH
from ordeq_dev_tools.pipelines.shared import packages
from ordeq_toml import TOML

API_DIR = ROOT_PATH / "docs" / "api"


@node
def clear_api_docs() -> None:
    """Clear the API_DIR, retaining .nav.yml and .gitignore files.

    Removes all files and directories in API_DIR except for .nav.yml and
    .gitignore. Creates API_DIR if it does not exist.
    """
    API_DIR.mkdir(parents=True, exist_ok=True)
    for item in API_DIR.iterdir():
        if item.name in {".nav.yml", ".gitignore"}:
            continue
        if item.is_dir():
            shutil.rmtree(item)
        else:
            item.unlink()


@node(inputs=packages)
def filter_packages(packages: list[str]) -> list[str]:
    """Filter out excluded packages.

    Args:
        packages: List of all package names.

    Returns:
        Filtered list of packages excluding test packages and dev tools.
    """
    excluded = {
        "ordeq-test-examples",
        "ordeq-dev-tools",
        "ordeq-test-utils",
    }
    return [pkg for pkg in packages if pkg not in excluded]


@node(inputs=filter_packages)
def check_ios_packages(packages: list[str]) -> list[tuple[str, bool]]:
    """Check which packages are iOS group packages.

    Args:
        packages: List of package names to check.

    Returns:
        List of tuples with (package_name, is_ios_group).
    """
    result = []
    for package_name in packages:
        package_dir = PACKAGES_PATH / package_name
        pyproject_path = package_dir / "pyproject.toml"

        is_ios = False
        if pyproject_path.exists():
            try:
                data = TOML(path=pyproject_path).load()
                tool_section = data.get("tool", {})
                ordeq_dev_section = tool_section.get("ordeq-dev", {})
                is_ios = ordeq_dev_section.get("group") == "ios"
            except Exception:
                is_ios = False

        result.append((package_name, is_ios))

    return result


@node(inputs=[clear_api_docs, check_ios_packages])
def generate_package_docs(_: None, package_info: list[tuple[str, bool]]) -> list[str]:
    """Generate API documentation files for all packages.

    Args:
        _: Clear docs completion signal (unused).
        package_info: List of (package_name, is_ios_group) tuples.

    Returns:
        List of created documentation file paths.
    """
    created_files = []

    for package_name, is_ios_group in package_info:
        package_dir = PACKAGES_PATH / package_name
        package_src = package_dir / "src"

        if not package_src.exists():
            continue

        if is_ios_group:
            # Generate single file for ios packages
            # Find the main module directory (should be only one)
            module_dirs = [
                d
                for d in package_src.iterdir()
                if d.is_dir() and not d.name.endswith(".egg-info")
            ]
            if module_dirs:
                main_module = module_dirs[0]  # Take the first (should be only one)
                module_name = main_module.name

                # Create single documentation file
                full_doc_path = API_DIR / f"{module_name}.md"
                full_doc_path.parent.mkdir(parents=True, exist_ok=True)

                content = f"---\ntitle: {module_name}\n---\n\n::: {module_name}\n"
                full_doc_path.write_text(content, encoding="utf-8")
                created_files.append(str(full_doc_path.relative_to(ROOT_PATH)))
        else:
            # Existing behavior for non-ios packages
            for module in sorted(package_src.rglob("*.py")):
                module_path = module.relative_to(package_src).with_suffix("")
                parts = tuple(module_path.parts)

                if parts[-1] in {"__main__", "_version", "__init__"}:
                    continue

                module_name = parts[-1]
                output_name = module_name

                full_doc_path = API_DIR / module_path.with_name(f"{output_name}.md")
                full_doc_path.parent.mkdir(parents=True, exist_ok=True)

                identifier = ".".join(parts)
                content = f"---\ntitle: {module_name}.py\n---\n\n::: {identifier}\n"
                full_doc_path.write_text(content, encoding="utf-8")
                created_files.append(str(full_doc_path.relative_to(ROOT_PATH)))

    return created_files


@node(inputs=generate_package_docs)
def generate_api_readmes(_: list[str]) -> None:
    """Generate a README.md in each top-level docs/api/*/ directory.

    The README.md will contain a Markdown H1 title using the directory name.

    Args:
        _: List of created documentation files (for dependency).
    """
    for subdir in API_DIR.iterdir():
        if subdir.is_dir():
            readme = subdir / "README.md"
            title = f"# {subdir.name}\n"
            readme.write_text(title, encoding="utf-8")
