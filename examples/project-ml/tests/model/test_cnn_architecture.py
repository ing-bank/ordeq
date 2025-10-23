import torch
from model.cnn_architecture import DigitCNN


def test_model_creation():
    """Test that we can create a model."""
    model = DigitCNN()
    assert model is not None


def test_model_forward_pass():
    """Test that model can process input."""
    model = DigitCNN()
    x = torch.randn(1, 1, 28, 28)  # Single MNIST image
    output = model(x)
    assert output.shape == (1, 10)  # 10 classes
