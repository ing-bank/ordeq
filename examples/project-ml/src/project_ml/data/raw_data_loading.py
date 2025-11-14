import logging
from typing import Any

import torch
from ordeq import node
from torchvision import transforms
from torchvision.datasets import VisionDataset
from torchvision.datasets.vision import StandardTransform

from project_ml import catalog

logger = logging.getLogger(__name__)


@node(inputs=[catalog.mnist_moments])
def transform(moments):
    mnist_mean, mnist_std = moments
    return transforms.Compose(
        [
            transforms.ToTensor(),
            transforms.Normalize((mnist_mean,), (mnist_std,)),  # MNIST mean and std
        ]
    )


@node(
    inputs=[catalog.train_dataset, transform],
)
def raw_mnist_train_data(train_dataset: VisionDataset, transform) -> dict[str, Any]:
    """Download the raw MNIST dataset."""
    train_dataset.transform = transform
    train_dataset.transforms = StandardTransform(transform)

    # Convert to tensors
    train_data = torch.stack([train_dataset[i][0] for i in range(len(train_dataset))])
    train_labels = torch.tensor(
        [train_dataset[i][1] for i in range(len(train_dataset))]
    )

    logger.info(
        "Loaded %d training samples",
        len(train_data),
    )

    return {
        "train_data": train_data,
        "train_labels": train_labels,
    }


@node(inputs=[catalog.test_dataset, transform])
def raw_mnist_test_data(test_dataset, transform):
    test_dataset.transform = transform
    test_dataset.transforms = StandardTransform(transform)

    test_data = torch.stack([test_dataset[i][0] for i in range(len(test_dataset))])
    test_labels = torch.tensor([test_dataset[i][1] for i in range(len(test_dataset))])

    logger.info(
        "Loaded %d test samples",
        len(test_data),
    )
    return {
        "test_data": test_data,
        "test_labels": test_labels,
    }
