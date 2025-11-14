from ordeq._resource import Resource

def test_resource_eq():
    a = Resource("path")
    b = Resource("path")
    assert a is not b
    assert a == b
    assert hash(a) == hash(b)

def test_resource_neq():
    a = Resource("a")
    b = Resource("b")
    assert a is not b
    assert a != b
    assert hash(a) != hash(b)