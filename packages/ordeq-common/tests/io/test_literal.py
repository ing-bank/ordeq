from ordeq_common import Literal


def test_it_loads():
    assert Literal("someValue").load() == "someValue"


def test_it_is_unique():
    a, b = Literal(""), Literal("")
    assert a is not b
    assert a != b
    assert hash(a) != hash(b)
