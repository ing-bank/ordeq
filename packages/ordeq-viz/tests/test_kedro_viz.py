import json

from ordeq._nodes import get_node

from ordeq_viz.graph import _gather_graph
from ordeq_viz.to_kedro_viz import graph_to_kedro_viz


def test_kedro(tmp_path):
    from example_1 import nodes as mod

    graph_to_kedro_viz(
        _gather_graph(
            nodes=[get_node(mod.world)], ios={"...": {"x": mod.x, "y": mod.y}}
        ),
        output_directory=tmp_path / "viz",
    )

    text = (tmp_path / "viz" / "api" / "main").read_text()
    data = json.loads(text)
    assert "nodes" in data
    assert len(data["nodes"]) == 3
    assert "edges" in data
    assert len(data["edges"]) == 2
