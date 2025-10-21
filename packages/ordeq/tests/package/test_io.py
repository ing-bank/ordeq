from dataclasses import dataclass

import pytest
from ordeq import IO, Input, IOException, Output


def test_standalone_input():
    i, j = Input(), Input()
    with pytest.raises(IOException):
        i.load()

    assert repr(i) == f"Input(idx={i._idx})"
    assert i != j
    assert i == i  # noqa: PLR0124
    assert j == j  # noqa: PLR0124
    assert i._idx != j._idx


def test_standalone_output():
    k, x = Output(), Output()
    k.save("test")  # does nothing

    assert repr(k) == f"Output(idx={k._idx})"
    assert k != x
    assert k == k  # noqa: PLR0124
    assert x == x  # noqa: PLR0124
    assert k._idx != x._idx


def test_standalone_io():
    y, z = IO(), IO()
    with pytest.raises(IOException):
        y.load()
    y.save("test")  # does nothing

    assert repr(y) == f"IO(idx={y._idx})"
    assert y != z
    assert y == y  # noqa: PLR0124
    assert z == z  # noqa: PLR0124
    assert y._idx != z._idx


@dataclass(frozen=True)
class CustomDataclassIO(IO[str]):
    attr: str

    def load(self, extra: str = "") -> str:
        return self.attr + extra

    def save(self, value: str, suffix: str = ""):
        self.attr += value + suffix


class CustomIO(IO[str]):
    def __init__(self, attr: str):
        self.attr = attr
        super().__init__()

    def load(self, extra: str = "") -> str:
        return self.attr + extra

    def save(self, value: str, suffix: str = ""):
        self.attr += value + suffix


@pytest.mark.parametrize("io", [CustomIO("attr"), CustomDataclassIO("attr")])
def test_load_save_options(io: IO):
    # All IO instances need to be hashable
    # TODO: Check hashability in a metaclass
    # TODO: Also check for existence of a __repr__

    hash(io)
    io_wlo = io.with_load_options(extra="extra")
    hash(io_wlo)
    io_wso = io.with_save_options(suffix="_suffix")
    hash(io_wso)
