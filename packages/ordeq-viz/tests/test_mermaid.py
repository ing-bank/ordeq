import pytest
from ordeq.framework import get_node

from ordeq_viz.gather import gather_nodes_and_ios_from_package
from ordeq_viz.to_mermaid import _make_mermaid_header, pipeline_to_mermaid


def test_mermaid():
    from example import nodes as mod  # ty: ignore[unresolved-import]

    diagram = pipeline_to_mermaid(
        nodes={get_node(mod.world)}, datasets={"x": mod.x, "y": mod.y}
    )

    assert diagram.startswith("graph TB")
    assert "world:::function" in diagram
    assert "[(x)]:::dataset0" in diagram
    assert "[(y)]:::dataset0" in diagram


def test_mermaid_wrapped():
    import example  # ty: ignore[unresolved-import]

    nodes, ios = gather_nodes_and_ios_from_package(example)
    diagram = pipeline_to_mermaid(nodes=nodes, datasets=ios)

    assert "-.->|name|" in diagram
    assert "-.->|writer|" in diagram

    diagram = pipeline_to_mermaid(
        nodes=nodes, datasets=ios, connect_wrapped_datasets=False
    )

    assert "-.->|name|" not in diagram
    assert "-.->|writer|" not in diagram


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
