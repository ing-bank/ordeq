import math
from pathlib import Path

import pytest
import torch
from ordeq_torch import TorchObject
from torch import nn


class SimpleModel(nn.Module):
    """Simple test model for object serialization."""

    def __init__(self, size: int):
        super().__init__()
        self.linear = nn.Linear(size, size)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.linear(x)


def test_torch_object_tensor_save_load(tmp_path: Path) -> None:
    """Test saving and loading tensors."""
    object_path = tmp_path / "tensor.pt"

    # Create a tensor
    original_tensor = torch.randn(3, 4, 5)

    # Save the tensor
    io = TorchObject(path=object_path)
    io.save(original_tensor)
    assert object_path.exists()

    # Load the tensor
    loaded_tensor = io.load()

    # Verify the loaded tensor
    assert isinstance(loaded_tensor, torch.Tensor)
    assert torch.equal(original_tensor, loaded_tensor)
    assert original_tensor.shape == loaded_tensor.shape
    assert original_tensor.dtype == loaded_tensor.dtype


def test_torch_object_list_of_tensors(tmp_path: Path) -> None:
    """Test saving and loading lists of tensors."""
    object_path = tmp_path / "tensor_list.pt"

    # Create a list of tensors
    original_data = [torch.randn(2, 3), torch.zeros(4, 5), torch.ones(1, 6)]

    # Save the list
    io = TorchObject(path=object_path)
    io.save(original_data)

    # Load the list
    loaded_data = io.load()

    # Verify the loaded data
    assert isinstance(loaded_data, list)
    assert len(loaded_data) == len(original_data)

    for original, loaded in zip(original_data, loaded_data, strict=False):
        assert torch.equal(original, loaded)


def test_torch_object_dict_with_tensors(tmp_path: Path) -> None:
    """Test saving and loading dictionaries containing tensors."""
    object_path = tmp_path / "tensor_dict.pt"

    # Create a dictionary with tensors
    original_data = {
        "weights": torch.randn(5, 10),
        "biases": torch.zeros(10),
        "metadata": {
            "name": "test_model",
            "version": 1,
            "params": torch.ones(3),
        },
        "list_data": [torch.randn(2, 2), torch.eye(3)],
    }

    # Save the dictionary
    io = TorchObject(path=object_path)
    io.save(original_data)

    # Load the dictionary
    loaded_data = io.load()

    # Verify the loaded data
    assert isinstance(loaded_data, dict)
    assert set(loaded_data.keys()) == set(original_data.keys())

    # Check tensor values
    assert torch.equal(original_data["weights"], loaded_data["weights"])
    assert torch.equal(original_data["biases"], loaded_data["biases"])
    assert torch.equal(
        original_data["metadata"]["params"], loaded_data["metadata"]["params"]
    )

    # Check metadata
    assert loaded_data["metadata"]["name"] == "test_model"
    assert loaded_data["metadata"]["version"] == 1

    # Check list data
    for orig, loaded in zip(
        original_data["list_data"], loaded_data["list_data"], strict=False
    ):
        assert torch.equal(orig, loaded)


def test_torch_object_state_dict(tmp_path: Path) -> None:
    """Test saving and loading model state dictionaries."""
    object_path = tmp_path / "state_dict.pt"

    # Create a model and get its state dict
    model = SimpleModel(size=8)
    model.linear.weight.data.fill_(1.5)
    model.linear.bias.data.fill_(0.25)
    original_state_dict = model.state_dict()

    # Save the state dict
    io = TorchObject(path=object_path)
    io.save(original_state_dict)

    # Load the state dict
    loaded_state_dict = io.load()

    # Verify the loaded state dict
    assert isinstance(loaded_state_dict, dict)
    assert set(loaded_state_dict.keys()) == set(original_state_dict.keys())

    for key in original_state_dict:
        assert torch.equal(original_state_dict[key], loaded_state_dict[key])

    # Verify we can load it into a new model
    new_model = SimpleModel(size=8)
    new_model.load_state_dict(loaded_state_dict)

    # Test that the models produce the same output
    test_input = torch.randn(1, 8)
    with torch.no_grad():
        original_output = model(test_input)
        new_output = new_model(test_input)
    assert torch.equal(original_output, new_output)


@pytest.mark.parametrize(
    "tensor_shape", [(5,), (3, 4), (2, 3, 4), (1, 2, 3, 4)]
)
def test_torch_object_different_tensor_shapes(
    tmp_path: Path, tensor_shape: tuple
) -> None:
    """Test tensors with different shapes."""
    object_path = tmp_path / f"tensor_{'x'.join(map(str, tensor_shape))}.pt"

    # Create tensor with specific shape
    original_tensor = torch.randn(*tensor_shape)

    # Save and load
    io = TorchObject(path=object_path)
    io.save(original_tensor)
    loaded_tensor = io.load()

    # Verify shape and values
    assert loaded_tensor.shape == tensor_shape
    assert torch.equal(original_tensor, loaded_tensor)


@pytest.mark.parametrize(
    "dtype",
    [torch.float32, torch.float64, torch.int32, torch.int64, torch.bool],
)
def test_torch_object_different_dtypes(
    tmp_path: Path, dtype: torch.dtype
) -> None:
    """Test tensors with different data types."""
    object_path = tmp_path / f"tensor_{str(dtype).split('.')[-1]}.pt"

    # Create tensor with specific dtype
    if dtype == torch.bool:
        original_tensor = torch.randint(0, 2, (3, 3), dtype=dtype)
    elif dtype in {torch.int32, torch.int64}:
        original_tensor = torch.randint(-10, 10, (3, 3), dtype=dtype)
    else:
        original_tensor = torch.randn(3, 3, dtype=dtype)

    # Save and load
    io = TorchObject(path=object_path)
    io.save(original_tensor)
    loaded_tensor = io.load()

    # Verify dtype and values
    assert loaded_tensor.dtype == dtype
    assert torch.equal(original_tensor, loaded_tensor)


def test_torch_object_mixed_python_types(tmp_path: Path) -> None:
    """Test saving mixed Python and PyTorch objects."""
    object_path = tmp_path / "mixed_data.pt"

    # Create mixed data structure
    original_data = {
        "string": "hello world",
        "int": 42,
        "float": math.pi,
        "list": [1, 2, 3, "nested"],
        "tensor": torch.randn(2, 2),
        "nested": {
            "bool": True,
            "none": None,
            "tensor_list": [torch.zeros(3), torch.ones(3)],
        },
    }

    # Save and load
    io = TorchObject(path=object_path)
    io.save(original_data)
    loaded_data = io.load()

    # Verify structure and values
    assert loaded_data["string"] == "hello world"
    assert loaded_data["int"] == 42
    assert loaded_data["float"] == math.pi
    assert loaded_data["list"] == [1, 2, 3, "nested"]
    assert torch.equal(original_data["tensor"], loaded_data["tensor"])
    assert loaded_data["nested"]["bool"] is True
    assert loaded_data["nested"]["none"] is None

    for orig, loaded in zip(
        original_data["nested"]["tensor_list"],
        loaded_data["nested"]["tensor_list"],
        strict=False,
    ):
        assert torch.equal(orig, loaded)
