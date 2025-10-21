from unittest.mock import MagicMock, patch

from ordeq_huggingface.disk_dataset import HuggingfaceDiskDataset


def test_init_sets_path():
    ds = HuggingfaceDiskDataset(path="some/path")
    assert ds.path == "some/path"


@patch("ordeq_huggingface.disk_dataset.load_from_disk")
def test_load_calls_load_from_disk(mock_load_from_disk):
    mock_result = MagicMock()
    mock_load_from_disk.return_value = mock_result
    ds = HuggingfaceDiskDataset(path="disk/path")
    result = ds.load(foo=1)
    mock_load_from_disk.assert_called_once_with("disk/path", foo=1)
    assert result is mock_result


def test_save_calls_save_to_disk():
    ds = HuggingfaceDiskDataset(path="disk/path")
    mock_data = MagicMock()
    ds.save(mock_data, bar=2)
    mock_data.save_to_disk.assert_called_once_with("disk/path", bar=2)
