from pathlib import Path

import pytest
import torch
from ordeq import IOException
from ordeq_torch import TorchModel
from torch import nn


class SimpleLinearModel(nn.Module):
    def __init__(self, input_size: int, output_size: int):
        super().__init__()
        self.linear = nn.Linear(input_size, output_size)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.linear(x)


class MultiLayerModel(nn.Module):
    def __init__(self, input_size: int, hidden_size: int, output_size: int):
        super().__init__()
        self.layers = nn.Sequential(
            nn.Linear(input_size, hidden_size),
            nn.ReLU(),
            nn.Linear(hidden_size, output_size),
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.layers(x)


def test_torch_model_save_and_load(tmp_path: Path) -> None:
    model_path = tmp_path / "model.pth"

    # Create and configure original model
    original_model = SimpleLinearModel(input_size=10, output_size=5)
    original_model.linear.weight.data.fill_(1.0)
    original_model.linear.bias.data.fill_(0.5)

    # Save the model
    io = TorchModel(
        path=model_path, model_class=SimpleLinearModel, model_args=(10, 5)
    )
    io.save(original_model)
    assert model_path.exists()

    # Load the model
    loaded_model = io.load()

    # Verify the loaded model
    assert isinstance(loaded_model, SimpleLinearModel)
    assert loaded_model.training is False  # Should be in eval mode

    # Check that weights are preserved
    assert torch.allclose(
        original_model.linear.weight, loaded_model.linear.weight
    )
    assert torch.allclose(original_model.linear.bias, loaded_model.linear.bias)


def test_torch_model_with_kwargs(tmp_path: Path) -> None:
    model_path = tmp_path / "model_kwargs.pth"

    # Create original model
    original_model = MultiLayerModel(
        input_size=8, hidden_size=16, output_size=4
    )

    # Save the model
    io = TorchModel(
        path=model_path,
        model_class=MultiLayerModel,
        model_args=(8,),
        model_kwargs={"hidden_size": 16, "output_size": 4},
    )
    io.save(original_model)

    # Load the model
    loaded_model = io.load()

    # Verify structure
    assert isinstance(loaded_model, MultiLayerModel)
    assert len(loaded_model.layers) == 3

    # Test forward pass to ensure model works
    test_input = torch.randn(1, 8)
    with torch.no_grad():
        original_output = original_model(test_input)
        loaded_output = loaded_model(test_input)

    assert torch.allclose(original_output, loaded_output)


def test_torch_model_load_without_model_class() -> None:
    io = TorchModel(path=Path("dummy.pth"))

    with pytest.raises(IOException, match="model_class must be provided"):
        io.load()


@pytest.mark.parametrize(
    ("input_size", "output_size"), [(5, 3), (10, 1), (1, 10)]
)
def test_torch_model_different_sizes(
    tmp_path: Path, input_size: int, output_size: int
) -> None:
    model_path = tmp_path / f"model_{input_size}_{output_size}.pth"

    # Create and train a simple model
    original_model = SimpleLinearModel(input_size, output_size)

    # Set some specific weights for testing
    with torch.no_grad():
        original_model.linear.weight.fill_(2.0)
        original_model.linear.bias.fill_(-1.0)

    # Save and load
    io = TorchModel(
        path=model_path,
        model_class=SimpleLinearModel,
        model_args=(input_size, output_size),
    )
    io.save(original_model)
    loaded_model = io.load()

    # Verify shapes are correct
    assert loaded_model.linear.weight.shape == (output_size, input_size)
    assert loaded_model.linear.bias.shape == (output_size,)

    # Verify values are preserved
    assert torch.allclose(
        original_model.linear.weight, loaded_model.linear.weight
    )
    assert torch.allclose(original_model.linear.bias, loaded_model.linear.bias)
