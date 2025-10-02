from pathlib import Path

import networkx as nx
from ordeq_networkx import NetworkxGML


def make_simple_graph():
    G = nx.Graph()
    G.add_edge("a", "b")
    return G


def make_graph_with_attrs():
    G = nx.Graph()
    G.add_node("x", color="red")
    G.add_edge("x", "y", weight=3)
    return G


def test_load_gml(tmp_path: Path):
    G = make_simple_graph()
    gml_path = tmp_path / "test.gml"
    nx.write_gml(G, gml_path)
    io = NetworkxGML(path=gml_path)
    loaded = io.load()
    assert nx.is_isomorphic(G, loaded)


def test_save_gml(tmp_path: Path):
    G = make_simple_graph()
    gml_path = tmp_path / "test2.gml"
    io = NetworkxGML(path=gml_path)
    io.save(G)
    loaded = nx.read_gml(gml_path)
    assert nx.is_isomorphic(G, loaded)


def test_roundtrip_gml(tmp_path: Path):
    G = make_graph_with_attrs()
    gml_path = tmp_path / "test3.gml"
    io = NetworkxGML(path=gml_path)
    io.save(G)
    loaded = io.load()
    assert nx.is_isomorphic(G, loaded)
    # Check node and edge attributes
    for n, d in G.nodes(data=True):
        assert loaded.nodes[n] == d
    for u, v, d in G.edges(data=True):
        assert loaded.edges[u, v] == d


def test_empty_graph(tmp_path: Path):
    G = nx.Graph()
    gml_path = tmp_path / "empty.gml"
    io = NetworkxGML(path=gml_path)
    io.save(G)
    loaded = io.load()
    assert nx.is_isomorphic(G, loaded)
    assert len(loaded.nodes) == 0
    assert len(loaded.edges) == 0
