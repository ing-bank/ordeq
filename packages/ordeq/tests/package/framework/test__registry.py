import pytest
from ordeq import Node
from ordeq._registry import Registry


def f():
    pass


def test_it_sets():
    registry = Registry()

    n = Node(func=f, inputs=(), outputs=())
    registry.set(f, n)
    assert registry._data[f] == n


def test_it_gets():
    registry = Registry()

    n = Node(func=f, inputs=(), outputs=())
    registry._data[f] = n
    assert registry.get(f) == n


def test_it_errors_when_set_twice():
    registry = Registry()

    n = Node(func=f, inputs=(), outputs=())
    registry.set(f, n)
    with pytest.raises(KeyError, match=r"Key '.+' already exists"):
        registry.set(f, n)


def test_it_contains():
    registry = Registry()

    n = Node(func=f, inputs=(), outputs=())
    registry.set(f, n)
    assert f in registry

    def unregistered(): ...

    assert unregistered not in registry
