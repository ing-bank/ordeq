import logging
from typing import Any

import torch
from torch import nn, optim

from project_ml.config.model_config import ModelConfig

logger = logging.getLogger(__name__)


def get_optimizer(config: Any, model_params) -> torch.optim.Optimizer:
    """Get optimizer based on config."""
    if config.optimizer_type.lower() == "adam":
        return optim.Adam(
            model_params,
            lr=config.learning_rate,
            weight_decay=config.weight_decay,
        )
    if config.optimizer_type.lower() == "sgd":
        return optim.SGD(
            model_params,
            lr=config.learning_rate,
            momentum=config.momentum,
            weight_decay=config.weight_decay,
        )
    return optim.Adam(
        model_params, lr=config.learning_rate, weight_decay=config.weight_decay
    )


def train_model(
    model: nn.Module, train_loader, val_loader, config: ModelConfig, device
):
    """Train the digit classification model with configurable parameters."""
    logger.info("Training on device: %s", device)
    model.to(device)

    # Get optimizer using utility function
    optimizer = get_optimizer(config, model.parameters())
    logger.info(
        f"Using {config.optimizer_type} optimizer with lr={config.learning_rate}"
    )

    criterion = nn.CrossEntropyLoss()

    # Add learning rate scheduler
    scheduler = None
    if config.use_lr_scheduler:
        scheduler = optim.lr_scheduler.StepLR(
            optimizer, step_size=config.lr_step_size, gamma=config.lr_gamma
        )
        logger.info(
            "Using StepLR scheduler with step_size=%s, gamma=%s",
            config.lr_step_size,
            config.lr_gamma,
        )

    train_losses = []
    val_accuracies = []

    # Early stopping variables
    best_val_accuracy = 0.0
    patience_counter = 0

    # Log training configuration
    logger.info("Starting training with:")
    logger.info(f"- Batch size: {config.batch_size}")
    logger.info(f"- Max epochs: {config.epochs}")
    logger.info("- Early stopping patience: %s", config.patience)
    logger.info(f"- Model architecture:\n{model!s}")

    for epoch in range(config.epochs):
        # Training phase
        model.train()
        train_loss = 0
        batch_count = 0
        correct_train = 0
        total_train = 0

        for batch_idx, (data, target) in enumerate(train_loader):
            _data, _target = data.to(device), target.to(device)
            optimizer.zero_grad()
            output = model(_data)
            loss = criterion(output, _target)
            loss.backward()
            optimizer.step()

            train_loss += loss.item()
            batch_count += 1

            # Calculate training accuracy
            _, predicted = torch.max(output.data, 1)
            total_train += target.size(0)
            correct_train += (predicted == target).sum().item()

            # Log progress every 100 batches
            if (batch_idx + 1) % 100 == 0:
                logger.debug(
                    f"Epoch {epoch + 1}/{config.epochs} "
                    f"[{batch_idx + 1}/{len(train_loader)}] "
                    f"Loss: {loss.item():.4f}"
                )

        avg_train_loss = train_loss / batch_count
        train_accuracy = 100 * correct_train / total_train
        train_losses.append(avg_train_loss)

        # Validation phase
        model.eval()
        val_correct = 0
        val_total = 0
        val_loss = 0

        with torch.no_grad():
            for data, target in val_loader:
                _data, _target = data.to(device), target.to(device)
                outputs = model(_data)
                val_loss += criterion(outputs, _target).item()
                _, predicted = torch.max(outputs.data, 1)
                val_total += _target.size(0)
                val_correct += (predicted == _target).sum().item()

        val_accuracy = 100 * val_correct / val_total
        avg_val_loss = val_loss / len(val_loader)
        val_accuracies.append(val_accuracy)

        # Log epoch results
        logger.info(
            f"Epoch {epoch + 1}/{config.epochs} - "
            f"Train Loss: {avg_train_loss:.4f} - "
            f"Train Acc: {train_accuracy:.2f}% - "
            f"Val Loss: {avg_val_loss:.4f} - "
            f"Val Acc: {val_accuracy:.2f}% - "
            f"LR: {optimizer.param_groups[0]['lr']:.6f}"
        )

        # Early stopping logic
        if config.use_early_stopping:
            if val_accuracy > best_val_accuracy + config.min_delta:
                best_val_accuracy = val_accuracy
                patience_counter = 0
                logger.info(f"New best validation accuracy: {best_val_accuracy:.2f}%")
            else:
                patience_counter += 1
                logger.info(
                    f"Validation accuracy did not improve. "
                    f"Best: {best_val_accuracy:.2f}% "
                    f"Current: {val_accuracy:.2f}% "
                    f"Patience: {patience_counter}/{config.patience}"
                )

            if patience_counter >= config.patience:
                logger.warning(
                    f"Early stopping triggered after {epoch + 1} epochs. "
                    f"Best validation accuracy: {best_val_accuracy:.2f}%"
                )
                break

        # Step the learning rate scheduler
        if scheduler is not None:
            scheduler.step()
            logger.debug(
                f"Learning rate adjusted to: {optimizer.param_groups[0]['lr']:.6f}"
            )

    # Final training summary
    logger.info("Training completed:")
    logger.info(f"- Best validation accuracy: {best_val_accuracy:.2f}%")
    logger.info(f"- Final learning rate: {optimizer.param_groups[0]['lr']:.6f}")
    logger.info(f"- Total epochs run: {epoch + 1}")

    return model, train_losses, val_accuracies
