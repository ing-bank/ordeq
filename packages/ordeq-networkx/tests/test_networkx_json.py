from pathlib import Path

import networkx as nx
from ordeq_networkx import NetworkxJSON


def make_simple_graph():
    G = nx.Graph()
    G.add_edge("a", "b")
    return G


def make_graph_with_attrs():
    G = nx.Graph()
    G.add_node("x", color="red")
    G.add_edge("x", "y", weight=3)
    return G


def test_load_json(tmp_path: Path):
    G = make_simple_graph()
    json_path = tmp_path / "test.json"
    nx.write_gml(G, json_path.with_suffix(".gml"))  # for reference
    nx.write_graphml(G, json_path.with_suffix(".graphml"))  # for reference
    nx.write_edgelist(G, json_path.with_suffix(".edgelist"))  # for reference
    nx.write_adjlist(G, json_path.with_suffix(".adjlist"))  # for reference
    nx.readwrite.json_graph.node_link_data(G)  # ensure import
    # Save as JSON using NetworkxJSON
    io = NetworkxJSON(path=json_path)
    io.save(G)
    loaded = io.load()
    assert nx.is_isomorphic(G, loaded)


def test_save_json(tmp_path: Path):
    G = make_simple_graph()
    json_path = tmp_path / "test2.json"
    io = NetworkxJSON(path=json_path)
    io.save(G)
    loaded = nx.readwrite.json_graph.node_link_graph(
        nx.readwrite.json_graph.node_link_data(G)
    )
    loaded2 = io.load()
    assert nx.is_isomorphic(G, loaded2)
    assert nx.is_isomorphic(loaded, loaded2)
    assert nx.is_isomorphic(loaded, G)


def test_roundtrip_json(tmp_path: Path):
    G = make_graph_with_attrs()
    json_path = tmp_path / "test3.json"
    io = NetworkxJSON(path=json_path)
    io.save(G)
    loaded = io.load()
    assert nx.is_isomorphic(G, loaded)
    # Check node and edge attributes
    for n, d in G.nodes(data=True):
        assert loaded.nodes[n] == d
    for u, v, d in G.edges(data=True):
        assert loaded.edges[u, v] == d


def test_empty_graph_json(tmp_path: Path):
    G = nx.Graph()
    json_path = tmp_path / "empty.json"
    io = NetworkxJSON(path=json_path)
    io.save(G)
    loaded = io.load()
    assert nx.is_isomorphic(G, loaded)
    assert len(loaded.nodes) == 0
    assert len(loaded.edges) == 0


def test_json_with_edge_and_node_attrs(tmp_path: Path):
    G = nx.Graph()
    G.add_node(1, label="foo")
    G.add_node(2, label="bar")
    G.add_edge(1, 2, weight=2.5)
    json_path = tmp_path / "attrs.json"
    io = NetworkxJSON(path=json_path)
    io.save(G)
    loaded = io.load()
    assert nx.is_isomorphic(G, loaded)
    # JSON preserves node ids as int, so compare directly
    assert {(n, tuple(sorted(d.items()))) for n, d in G.nodes(data=True)} == {
        (n, tuple(sorted(d.items()))) for n, d in loaded.nodes(data=True)
    }
    assert {
        (u, v, tuple(sorted(d.items()))) for u, v, d in G.edges(data=True)
    } == {
        (u, v, tuple(sorted(d.items()))) for u, v, d in loaded.edges(data=True)
    }
