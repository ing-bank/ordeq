from pathlib import Path

import networkx as nx
from ordeq_networkx import NetworkxGraphML


def make_simple_graph():
    G = nx.Graph()
    G.add_edge("a", "b")
    return G


def make_graph_with_attrs():
    G = nx.Graph()
    G.add_node("x", color="red")
    G.add_edge("x", "y", weight=3)
    return G


def test_load_graphml(tmp_path: Path):
    G = make_simple_graph()
    graphml_path = tmp_path / "test.graphml"
    nx.write_graphml(G, graphml_path)
    io = NetworkxGraphML(path=graphml_path)
    loaded = io.load()
    assert nx.is_isomorphic(G, loaded)


def test_save_graphml(tmp_path: Path):
    G = make_simple_graph()
    graphml_path = tmp_path / "test2.graphml"
    io = NetworkxGraphML(path=graphml_path)
    io.save(G)
    loaded = nx.read_graphml(graphml_path)
    assert nx.is_isomorphic(G, loaded)


def test_roundtrip_graphml(tmp_path: Path):
    G = make_graph_with_attrs()
    graphml_path = tmp_path / "test3.graphml"
    io = NetworkxGraphML(path=graphml_path)
    io.save(G)
    loaded = io.load()
    assert nx.is_isomorphic(G, loaded)
    # Check node and edge attributes
    for n, d in G.nodes(data=True):
        assert loaded.nodes[n] == d
    for u, v, d in G.edges(data=True):
        assert loaded.edges[u, v] == d


def test_empty_graph_graphml(tmp_path: Path):
    G = nx.Graph()
    graphml_path = tmp_path / "empty.graphml"
    io = NetworkxGraphML(path=graphml_path)
    io.save(G)
    loaded = io.load()
    assert nx.is_isomorphic(G, loaded)
    assert len(loaded.nodes) == 0
    assert len(loaded.edges) == 0


def test_graphml_with_edge_and_node_attrs(tmp_path: Path):
    G = nx.Graph()
    G.add_node(1, label="foo")
    G.add_node(2, label="bar")
    G.add_edge(1, 2, weight=2.5)
    graphml_path = tmp_path / "attrs.graphml"
    io = NetworkxGraphML(path=graphml_path)
    io.save(G)
    loaded = io.load()
    assert nx.is_isomorphic(G, loaded)

    # GraphML stores node ids as strings, so compare as strings
    assert {
        (str(n), tuple(sorted(d.items()))) for n, d in G.nodes(data=True)
    } == {(n, tuple(sorted(d.items()))) for n, d in loaded.nodes(data=True)}
    assert {
        (str(u), str(v), tuple(sorted(d.items())))
        for u, v, d in G.edges(data=True)
    } == {
        (u, v, tuple(sorted(d.items()))) for u, v, d in loaded.edges(data=True)
    }
