from starter_testing_nodes.pipeline import greet


def test_greet_empty():
    assert greet([]) == []


def test_greet_one_name():
    assert greet([["Alice"]]) == [["Hello, Alice!"]]


def test_greet_two_names():
    assert greet([["Alice"], ["Bob"]]) == [["Hello, Alice!"], ["Hello, Bob!"]]


def test_greet_special_chars():
    assert greet([["A$i%*c"]]) == [["Hello, A$i%*c!"]]
