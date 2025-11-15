import logging

import torch
from ordeq import node
from torch.utils.data import DataLoader, TensorDataset

from project_ml import catalog
from project_ml.config.model_config import ModelConfig
from project_ml.data.data_preprocessing import processed_mnist_train_data

logger = logging.getLogger(__name__)


@node(
    inputs=[processed_mnist_train_data, catalog.model_config],
)
def train_loader(
    processed_mnist_data: dict[str, torch.Tensor], config: ModelConfig
) -> DataLoader:
    """Create data loaders for training and validation datasets."""
    train_data = processed_mnist_data["train_data"]
    train_labels = processed_mnist_data["train_labels"]
    train_dataset = TensorDataset(train_data, train_labels)
    return DataLoader(train_dataset, batch_size=config.batch_size, shuffle=True)


@node(
    inputs=[processed_mnist_train_data, catalog.model_config],
)
def val_loader(
    processed_mnist_data: dict[str, torch.Tensor], config: ModelConfig
) -> DataLoader:
    """Create data loaders for training and validation datasets."""
    val_data = processed_mnist_data["val_data"]
    val_labels = processed_mnist_data["val_labels"]
    val_dataset = TensorDataset(val_data, val_labels)

    return DataLoader(val_dataset, batch_size=config.batch_size, shuffle=False)


@node
def training_device() -> torch.device:
    """Determine the device to use for training (CPU or GPU)."""
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    logger.info("Using device: %s", device)
    return device
