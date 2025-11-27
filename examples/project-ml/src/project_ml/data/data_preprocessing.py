import logging
from typing import Any

import torch
from ordeq import node
from sklearn.model_selection import train_test_split

from project_ml import catalog
from project_ml.data.raw_data_loading import raw_mnist_test_data, raw_mnist_train_data

logger = logging.getLogger(__name__)


@node(
    inputs=[raw_mnist_train_data, catalog.validation_split, catalog.random_seed],
)
def processed_mnist_train_data(
    raw_mnist_data: dict[str, Any], validation_split: float, random_seed: float
) -> dict[str, torch.Tensor]:
    """Process MNIST data and create train/validation split."""
    train_data = raw_mnist_data["train_data"]
    train_labels = raw_mnist_data["train_labels"]

    # Create validation split from training data
    train_data, val_data, train_labels, val_labels = train_test_split(
        train_data,
        train_labels,
        test_size=validation_split,
        random_state=random_seed,
        stratify=train_labels,
    )

    # Convert back to tensors
    train_data = torch.tensor(train_data)
    val_data = torch.tensor(val_data)
    train_labels = torch.tensor(train_labels)
    val_labels = torch.tensor(val_labels)

    data = {
        "train_data": train_data,
        "val_data": val_data,
        "train_labels": train_labels,
        "val_labels": val_labels,
    }

    logger.info(
        "Processed data - Train: %d, Val: %d, Num Classes: %d, Image Shape: %s",
        len(train_data),
        len(val_data),
        len(torch.unique(train_labels)),
        str(train_data.shape[1:]),
    )

    return data


@node(
    inputs=[raw_mnist_test_data],
)
def processed_mnist_test_data(
    raw_mnist_data: dict[str, Any],
) -> dict[str, torch.Tensor]:
    """Process MNIST test data."""
    test_data = raw_mnist_data["test_data"]
    test_labels = raw_mnist_data["test_labels"]

    data = {
        "test_data": test_data,
        "test_labels": test_labels,
    }

    logger.info(
        "Processed test data - Test: %d, Num Classes: %d, Image Shape: %s",
        len(test_data),
        len(torch.unique(test_labels)),
        str(test_data.shape[1:]),
    )

    return data
