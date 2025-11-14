import logging
from typing import Any

import torch
from ordeq import node
from sklearn.model_selection import train_test_split

from project_ml import catalog
from project_ml.data.raw_data_loading import raw_mnist_data

logger = logging.getLogger(__name__)


@node(
    inputs=[raw_mnist_data, catalog.validation_split, catalog.random_seed],
    outputs=[catalog.processed_data, catalog.data_metadata],
)
def processed_mnist_data(
    raw_mnist_data: dict[str, Any], validation_split: float, random_seed: float
) -> tuple[dict[str, torch.Tensor], dict[str, Any]]:
    """Process MNIST data and create train/validation split."""
    train_data = raw_mnist_data["train_data"]
    train_labels = raw_mnist_data["train_labels"]
    test_data = raw_mnist_data["test_data"]
    test_labels = raw_mnist_data["test_labels"]

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

    metadata = {
        "train_samples": len(train_data),
        "val_samples": len(val_data),
        "test_samples": len(test_data),
        "image_shape": str(train_data.shape[1:]),
        "num_classes": len(torch.unique(train_labels)),
    }
    data = {
        "train_data": train_data,
        "val_data": val_data,
        "train_labels": train_labels,
        "val_labels": val_labels,
        "test_data": test_data,
        "test_labels": test_labels,
    }

    logger.info(
        f"Processed data - Train: {len(train_data)}, Val: {len(val_data)}, Test: {len(test_data)}"
    )

    return data, metadata
