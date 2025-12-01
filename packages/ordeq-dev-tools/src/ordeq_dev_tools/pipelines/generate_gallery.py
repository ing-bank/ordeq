"""Pipeline to generate the gallery.md file with visualization grids."""

import sys
from pathlib import Path

from ordeq import node
from ordeq_files import Text

from ordeq_dev_tools.paths import ROOT_PATH

gallery_file = Text(path=ROOT_PATH / "docs" / "guides" / "gallery.md")


def _format_example_name(name: str) -> str:
    """Format example directory name for display."""
    # Convert kebab-case to title case
    return name.replace("-", " ").title()


def _get_example_description(example_dir: Path) -> str:
    """Get description for an example from its README.md file."""
    readme_path = example_dir / "README.md"
    try:
        readme_content = readme_path.read_text()
        # Try to extract first paragraph or heading description
        lines = readme_content.split("\n")
        for line in lines[1:]:  # Skip first line (usually title)
            line = line.strip()
            if line and not line.startswith("#"):
                return line
    except Exception:
        # Fallback if README can't be read
        return f"Example demonstrating {_format_example_name(example_dir.name).lower()} usage."

    # Fallback if no suitable description found
    return (
        f"Example demonstrating {_format_example_name(example_dir.name).lower()} usage."
    )


def _generate_example_visualization(example_dir: Path) -> str | None:
    """Generate mermaid visualization for an example directory."""
    try:
        # First check if there's already a mermaid file
        existing_mermaid = list(example_dir.rglob("*.mermaid"))
        if existing_mermaid:
            return existing_mermaid[0].read_text().strip()

    except Exception as e:
        print(
            f"Warning: Could not generate visualization for {example_dir.name}: {e}",
            file=sys.stderr,
        )

    return None


@node(outputs=gallery_file)
def generate_gallery() -> str:
    """Generate the gallery.md file with a grid of pipeline visualizations.

    Returns:
        The markdown content for the gallery page.
    """
    examples_path = ROOT_PATH / "examples"

    # Get all example directories (excluding files like .DS_Store and README.md)
    example_dirs = [
        d for d in examples_path.iterdir() if d.is_dir() and not d.name.startswith(".")
    ]

    # Sort alphabetically for consistent ordering
    example_dirs.sort(key=lambda d: d.name)

    # Start building the markdown content
    content_lines = [
        "# Example gallery",
        "",
        "Explore different Ordeq example pipelines.",
        "",
        '<div class="grid cards" markdown>',
        "",
    ]

    for example_dir in example_dirs:
        example_name = example_dir.name

        # Try to generate or find visualization for this example
        viz_content = _generate_example_visualization(example_dir)

        # Start building the card content - same structure for all cards
        card_content = [
            f"-   :material-graph: **{_format_example_name(example_name)}**",
            "",
            "    ---",
            "",
            f"    {_get_example_description(example_dir)}",
            "",
        ]

        # Add visualization section if available
        if viz_content:
            print(f"Visualization for {example_name}")
            # Indent mermaid content properly for markdown cards
            indented_viz = "\n".join(f"    {line}" for line in viz_content.split("\n"))

            card_content.extend(["    ```mermaid", indented_viz, "    ```", ""])
        else:
            if viz_content:
                print(
                    f"Visualization too short for {example_name} (length: {len(viz_content)})"
                )
            else:
                print(f"No visualization generated for {example_name}")

        # Always add the link at the bottom
        card_content.extend(
            [
                f"    [:octicons-arrow-right-24: View example](https://github.com/ing-bank/ordeq/tree/main/examples/{example_name})",
                "",
            ]
        )

        content_lines.extend(card_content)

    content_lines.append("</div>")

    return "\n".join(content_lines)


def _python_file_to_module_path(file_path: Path, base_dir: Path) -> str:
    """Convert a Python file path to a module path."""
    relative_path = file_path.relative_to(base_dir)
    module_parts = list(relative_path.parts[:-1])  # Remove file extension
    module_parts.append(relative_path.stem)
    return ".".join(module_parts)


def _find_pipeline_module(example_dir: Path) -> str | None:
    """Find the main pipeline module for an example."""
    # Check for single file examples
    python_files = list(example_dir.glob("*.py"))

    if len(python_files) == 1:
        module_path = _python_file_to_module_path(python_files[0], example_dir)
        return module_path

    # Check for package structure in root directory
    root_package_dirs = [
        d
        for d in example_dir.iterdir()
        if d.is_dir() and not d.name.startswith(".") and (d / "__init__.py").exists()
    ]

    if root_package_dirs:
        # Use first package found in root
        main_package = root_package_dirs[0]
        return main_package.name

    # Check for package structure in src directory
    src_dir = example_dir / "src"

    if src_dir.exists():
        # Check for single Python files in src directory first
        src_python_files = list(src_dir.glob("*.py"))

        if len(src_python_files) == 1:
            # Single file in src directory
            module_path = _python_file_to_module_path(src_python_files[0], src_dir)
            return module_path

        # Find the main package in src
        package_dirs = [
            d
            for d in src_dir.iterdir()
            if d.is_dir() and not d.name.endswith(".egg-info")
        ]

        if package_dirs:
            main_package = package_dirs[0]  # Take first package

            # Look for __main__.py or __init__.py
            if (main_package / "__main__.py").exists():
                module_name = f"{main_package.name}.__main__"
                return module_name
            elif (main_package / "__init__.py").exists():
                module_name = main_package.name
                return module_name

    return None
