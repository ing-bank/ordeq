import logging

import torch
from ordeq import node
from torch.utils.data import DataLoader, TensorDataset

from project_ml import catalog
from project_ml.config.model_config import ModelConfig
from project_ml.data.data_preprocessing import processed_mnist_train_data
from project_ml.model.cnn_architecture import DigitCNN
from project_ml.model.model_evaluation import training_device
from project_ml.model.train_model import train_model

logger = logging.getLogger(__name__)


@node(
    inputs=[processed_mnist_train_data, catalog.model_config],
    outputs=[catalog.train_loader, catalog.val_loader],
)
def create_data_loaders(
    processed_mnist_data: dict[str, torch.Tensor], config: ModelConfig
) -> tuple[DataLoader, DataLoader]:
    """Create data loaders for training and validation datasets."""
    train_data = processed_mnist_data["train_data"]
    val_data = processed_mnist_data["val_data"]
    train_labels = processed_mnist_data["train_labels"]
    val_labels = processed_mnist_data["val_labels"]

    train_dataset = TensorDataset(train_data, train_labels)
    val_dataset = TensorDataset(val_data, val_labels)

    train_loader = DataLoader(train_dataset, batch_size=config.batch_size, shuffle=True)
    val_loader = DataLoader(val_dataset, batch_size=config.batch_size, shuffle=False)

    return train_loader, val_loader


@node(
    inputs=[
        catalog.train_loader,
        catalog.val_loader,
        catalog.model_config,
        training_device,
    ],
    outputs=[catalog.model, catalog.training_metadata],
)
def digit_classifier(
    train_loader: DataLoader,
    val_loader: DataLoader,
    config: ModelConfig,
    device: torch.device,
) -> tuple[DigitCNN, dict]:
    """Train a CNN to classify handwritten digits 0-9 with flexible configuration."""
    logger.info("Training with config: %s", config)

    # Initialize model with configuration
    model = DigitCNN(config)

    # Train the model - pass context to train_model
    trained_model, train_losses, val_accuracies = train_model(
        model, train_loader, val_loader, config, device
    )

    final_val_accuracy = val_accuracies[-1]

    # Add metadata
    metadata = {
        "final_val_accuracy": final_val_accuracy,
        "training_epochs": len(train_losses),
        "configured_epochs": config.epochs,
        "model_parameters": sum(p.numel() for p in trained_model.parameters()),
        "final_train_loss": train_losses[-1],
        "learning_rate": config.learning_rate,
        "batch_size": config.batch_size,
        "optimizer": config.optimizer_type,
        "early_stopping_used": config.use_early_stopping,
    }

    logger.info(
        f"Model training completed. Final validation accuracy: {final_val_accuracy:.2f}%"
    )

    return trained_model, metadata
