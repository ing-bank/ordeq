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
            # Indent mermaid content properly for markdown cards
            indented_viz = "\n".join(f"    {line}" for line in viz_content.split("\n"))

            card_content.extend(["    ```mermaid", indented_viz, "    ```", ""])

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
