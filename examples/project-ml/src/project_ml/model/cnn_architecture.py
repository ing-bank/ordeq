import torch
import torch.nn.functional as F
from torch import nn

from project_ml.config.model_config import ModelConfig


class DigitCNN(nn.Module):
    """Improved CNN for MNIST digit classification based on research."""

    def __init__(self, config: ModelConfig):
        super().__init__()

        # First convolutional block
        self.conv1 = nn.Conv2d(
            1, config.conv1_channels, kernel_size=5, padding=2
        )  # 5x5 kernel, maintain size
        self.bn1 = (
            nn.BatchNorm2d(config.conv1_channels)
            if config.use_batch_norm
            else nn.Identity()
        )
        self.pool1 = nn.MaxPool2d(2, 2)  # 28x28 -> 14x14

        # Second convolutional block
        self.conv2 = nn.Conv2d(
            config.conv1_channels,
            config.conv2_channels,
            kernel_size=5,
            padding=2,
        )
        self.bn2 = (
            nn.BatchNorm2d(config.conv2_channels)
            if config.use_batch_norm
            else nn.Identity()
        )
        self.pool2 = nn.MaxPool2d(2, 2)  # 14x14 -> 7x7

        # Third convolutional block (new)
        self.conv3 = nn.Conv2d(
            config.conv2_channels,
            config.conv3_channels,
            kernel_size=3,
            padding=1,
        )
        self.bn3 = (
            nn.BatchNorm2d(config.conv3_channels)
            if config.use_batch_norm
            else nn.Identity()
        )
        self.pool3 = nn.AdaptiveAvgPool2d((3, 3))  # Adaptive pooling to 3x3

        # Dropout layers
        self.dropout1 = nn.Dropout2d(config.dropout1_rate)
        self.dropout2 = nn.Dropout(config.dropout2_rate)

        # Calculate the flattened size: 3x3 * conv3_channels
        conv_output_size = 3 * 3 * config.conv3_channels

        # Fully connected layers
        self.fc1 = nn.Linear(conv_output_size, config.hidden_size)
        self.fc2 = nn.Linear(
            config.hidden_size, config.hidden_size // 2
        )  # Additional FC layer
        self.fc3 = nn.Linear(config.hidden_size // 2, 10)

    def _conv_block(self, x, conv, bn, pool, dropout=None):
        """Apply a convolutional block: conv -> bn -> relu -> pool -> dropout (optional)."""
        x = conv(x)
        x = bn(x)
        x = F.relu(x)
        x = pool(x)
        if dropout is not None:
            x = dropout(x)
        return x

    def _fc_block(self, x, fc, dropout=None):
        """Apply a fully connected block: linear -> relu -> dropout (optional)."""
        x = fc(x)
        x = F.relu(x)
        if dropout is not None:
            x = dropout(x)
        return x

    def forward(self, x):
        """Forward pass through the CNN architecture.

        Input: (batch_size, 1, 28, 28) - MNIST digit images
        Output: (batch_size, 10) - Raw logits for 10 digit classes

        Architecture flow:
        1. Conv1: 28x28 -> 14x14 (5x5 kernel, 32 channels)
        2. Conv2: 14x14 -> 7x7 (5x5 kernel, 64 channels) + spatial dropout
        3. Conv3: 7x7 -> 3x3 (3x3 kernel, 128 channels, adaptive pooling)
        4. Flatten: 3x3*128 = 1152 features
        5. FC layers: 1152 -> 256 -> 128 -> 10 (with dropout)
        """
        # Convolutional layers with progressive downsampling
        x = self._conv_block(x, self.conv1, self.bn1, self.pool1)
        x = self._conv_block(x, self.conv2, self.bn2, self.pool2, self.dropout1)
        x = self._conv_block(x, self.conv3, self.bn3, self.pool3)

        # Flatten spatial dimensions for fully connected layers
        x = torch.flatten(x, 1)  # Keep batch dimension

        # Fully connected layers with progressive feature reduction
        x = self._fc_block(x, self.fc1, self.dropout2)
        x = self._fc_block(x, self.fc2)
        x = self.fc3(x)  # Final layer - no activation (raw logits)

        return x  # Return raw logits for CrossEntropyLoss
