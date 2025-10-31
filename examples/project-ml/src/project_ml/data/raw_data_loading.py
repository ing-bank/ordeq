import logging
from typing import Any

import catalog
import torch
from ordeq import node
from torchvision import transforms
from torchvision.datasets import VisionDataset
from torchvision.datasets.vision import StandardTransform

logger = logging.getLogger(__name__)


@node(
    inputs=[
        catalog.train_dataset,
        catalog.test_dataset,
        catalog.mnist_moments,
    ],
    outputs=catalog.raw_data,
)
def raw_mnist_data(
    train_dataset: VisionDataset,
    test_dataset: VisionDataset,
    moments: tuple[float, float],
) -> dict[str, Any]:
    """Download the raw MNIST dataset."""
    mnist_mean, mnist_std = moments
    transform = transforms.Compose(
        [
            transforms.ToTensor(),
            transforms.Normalize((mnist_mean,), (mnist_std,)),  # MNIST mean and std
        ]
    )
    train_dataset.transform = transform
    train_dataset.transforms = StandardTransform(transform)

    test_dataset.transform = transform
    test_dataset.transforms = StandardTransform(transform)

    # Convert to tensors
    train_data = torch.stack([train_dataset[i][0] for i in range(len(train_dataset))])
    train_labels = torch.tensor(
        [train_dataset[i][1] for i in range(len(train_dataset))]
    )

    test_data = torch.stack([test_dataset[i][0] for i in range(len(test_dataset))])
    test_labels = torch.tensor([test_dataset[i][1] for i in range(len(test_dataset))])

    logger.info(
        "Loaded %d training samples and %d test samples",
        len(train_data),
        len(test_data),
    )

    return {
        "train_data": train_data,
        "train_labels": train_labels,
        "test_data": test_data,
        "test_labels": test_labels,
    }
