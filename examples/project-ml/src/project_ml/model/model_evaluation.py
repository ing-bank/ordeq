import logging
from typing import Any

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import torch
from ordeq import node
from sklearn.metrics import classification_report, confusion_matrix
from torch.utils.data import DataLoader, TensorDataset

from project_ml import catalog
from project_ml.config.model_evaluation_config import ModelEvaluationConfig
from project_ml.data.data_preprocessing import processed_mnist_test_data

logger = logging.getLogger(__name__)


@node(
    inputs=[processed_mnist_test_data, catalog.model_evaluation_config],
    outputs=catalog.test_loader,
)
def create_test_loader(raw_mnist_data: dict[str, Any], config: ModelEvaluationConfig):
    test_data = raw_mnist_data["test_data"]
    test_labels = raw_mnist_data["test_labels"]

    test_dataset = TensorDataset(test_data, test_labels)
    return DataLoader(test_dataset, batch_size=config.batch_size, shuffle=False)


@node
def training_device() -> torch.device:
    """Determine the device to use for training (CPU or GPU)."""
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    logger.info("Using device: %s", device)
    return device


@node(
    inputs=[catalog.model, catalog.test_loader, training_device],
    outputs=[
        catalog.model_evaluation_result,
        catalog.confusion_matrix,
        catalog.model_evaluation_metadata,
    ],
    description="Evaluate model performance on test set",
)
def model_evaluation(model_to_evaluate, test_loader, device):
    """Evaluate the trained model on the test set."""
    model_to_evaluate.to(device)
    model_to_evaluate.eval()

    # Make predictions
    all_predictions = []
    all_labels = []

    with torch.no_grad():
        for data, target in test_loader:
            _data, _target = data.to(device), target.to(device)
            outputs = model_to_evaluate(_data)
            _, predicted = torch.max(outputs.data, 1)
            all_predictions.extend(predicted.cpu().numpy())
            all_labels.extend(_target.cpu().numpy())

    all_predictions = np.array(all_predictions)
    all_labels = np.array(all_labels)

    # Calculate metrics
    test_accuracy = float(np.mean(all_predictions == all_labels))

    # Create confusion matrix plot
    cm = confusion_matrix(all_labels, all_predictions)
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", ax=ax)
    ax.set_title("Confusion Matrix - Test Set")
    ax.set_xlabel("Predicted")
    ax.set_ylabel("Actual")

    # Generate classification report
    class_report = classification_report(all_labels, all_predictions, output_dict=True)

    metadata = {
        "test_accuracy": test_accuracy,
        "test_samples": len(all_labels),
        "precision_macro": float(class_report["macro avg"]["precision"]),
        "recall_macro": float(class_report["macro avg"]["recall"]),
        "f1_macro": float(class_report["macro avg"]["f1-score"]),
    }

    logger.info(f"Model evaluation completed. Test accuracy: {test_accuracy:.4f}")

    evaluation_results = {
        "test_accuracy": test_accuracy,
        "predictions": all_predictions.tolist(),
        "labels": all_labels.tolist(),
        "classification_report": class_report,
    }
    return evaluation_results, fig, metadata
