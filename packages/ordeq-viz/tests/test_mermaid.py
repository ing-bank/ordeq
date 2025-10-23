import pytest

from ordeq_viz.to_mermaid import _make_mermaid_header


@pytest.mark.parametrize(
    ("header_dict", "expected"),
    [
        # All fields None
        (
            {
                "title": None,
                "config": {"layout": None, "theme": None, "look": None},
            },
            "",
        ),
        # All config fields None, title provided
        (
            {
                "title": "My Diagram",
                "config": {"layout": None, "theme": None, "look": None},
            },
            '---\ntitle: "My Diagram"\n---\n',
        ),
        # All fields provided
        (
            {
                "title": "My Diagram",
                "config": {"layout": "dagre", "theme": "neo", "look": "neo"},
            },
            '---\ntitle: "My Diagram"\nconfig:\n  layout: dagre\n  '
            "theme: neo\n  look: neo\n---\n",
        ),
        # Only title
        (
            {"title": "Only Title", "config": {}},
            '---\ntitle: "Only Title"\n---\n',
        ),
        # Only layout
        (
            {
                "title": None,
                "config": {"layout": "dagre", "theme": None, "look": None},
            },
            "---\nconfig:\n  layout: dagre\n---\n",
        ),
        # Title and theme
        (
            {
                "title": "Title",
                "config": {"layout": None, "theme": "dark", "look": None},
            },
            '---\ntitle: "Title"\nconfig:\n  theme: dark\n---\n',
        ),
    ],
)
def test_mermaid_header_parametrized(header_dict, expected):
    result = _make_mermaid_header(header_dict)
    assert result == expected
