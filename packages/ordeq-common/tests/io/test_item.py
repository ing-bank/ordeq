import pytest
from ordeq import Input, IOException
from ordeq_common import Item
from ordeq_files import JSON, YAML
from ordeq_toml import TOML


class DummyInput(Input[dict]):
    def __init__(self, data):
        super().__init__()
        self._data = data

    def load(self):
        return self._data


@pytest.mark.parametrize(
    ("data", "key", "expected"),
    [
        ({"a": 1, "b": 2}, ("a",), 1),
        ({"a": {"b": 3}}, ("a", "b"), 3),
        ({"x": {"y": {"z": 42}}}, ("x", "y", "z"), 42),
        ({"foo": {"bar": {"baz": 7}}}, ("foo", "bar"), {"baz": 7}),
    ],
)
def test_item_load(data, key, expected):
    item = Item(DummyInput(data), key=key)
    assert item.load() == expected


def test_item_load_missing_key_returns_default():
    item = Item(DummyInput({"a": 1}), key=("b",), default=99)
    assert item.load() == 99


def test_item_load_missing_key_raises_keyerror():
    item = Item(DummyInput({"a": 1}), key=("b",))
    with pytest.raises(IOException):
        item.load()


def test_item_with_yaml(tmp_path):
    path = tmp_path / "test.yaml"
    path.write_text("foo:\n  bar: 1\n")
    item = Item(YAML(path=path), key=("foo", "bar"))
    assert item.load() == 1


def test_item_with_json(tmp_path):
    path = tmp_path / "test.json"
    path.write_text('{"foo": {"bar": 2}}')
    item = Item(JSON(path=path), key=("foo", "bar"))
    assert item.load() == 2


def test_item_with_toml(tmp_path):
    path = tmp_path / "test.toml"
    path.write_text("[foo]\nbar = 3\n")
    item = Item(TOML(path=path), key=("foo", "bar"))
    assert item.load() == 3
