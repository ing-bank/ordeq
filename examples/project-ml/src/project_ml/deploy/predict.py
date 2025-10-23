import logging
from typing import Any

import catalog
import numpy as np
import torch
from config.batch_prediction_config import BatchPredictionConfig
from config.real_time_prediction_config import RealTimePredictionConfig
from ordeq import node
from torch.utils.data import DataLoader, TensorDataset

logger = logging.getLogger(__name__)


@node(inputs=catalog.batch_prediction_config, outputs=catalog.dummy_images)
def generate_dummy_images(config: BatchPredictionConfig) -> torch.Tensor:
    # For demo purposes, create some test images
    return torch.randn(config.num_test_images, 1, 28, 28)


@node(inputs=catalog.real_time_prediction_config, outputs=catalog.dummy_batch)
def generate_dummy_batch(config: RealTimePredictionConfig):
    # For demo purposes, create some test images
    return torch.randn(config.batch_size, 1, 28, 28)


@node(inputs=catalog.batch_prediction_config, outputs=catalog.inference_device)
def select_inference_device(config: BatchPredictionConfig) -> str:
    """Select device for inference based on availability."""
    return torch.device(
        config.device
        if torch.cuda.is_available() and config.device == "cuda"
        else "cpu"
    )


@node(
    inputs=[
        catalog.dummy_images,
        catalog.production_model,
        catalog.batch_prediction_config,
        catalog.inference_device,
    ],
    outputs=[catalog.batch_predictions, catalog.batch_prediction_metadata],
)
def batch_digit_predictions(
    dummy_images, production_model, config: BatchPredictionConfig, device
) -> tuple[dict[str, list], Any]:
    """Process overnight batch of user-uploaded digit images."""
    production_model.to(device)
    production_model.eval()

    # Preprocess images
    processed_images = dummy_images.float() / 255.0

    dataset = TensorDataset(processed_images)
    dataloader = DataLoader(dataset, batch_size=config.batch_size, shuffle=False)

    predictions = []
    confidences = []

    with torch.no_grad():
        for (data,) in dataloader:
            _data = data.to(device)
            outputs = production_model(_data)
            probabilities = torch.softmax(outputs, dim=1)
            predicted_classes = torch.argmax(probabilities, dim=1)
            max_confidences = torch.max(probabilities, dim=1)[0]

            predictions.extend(predicted_classes.cpu().numpy().tolist())
            confidences.extend(max_confidences.cpu().numpy().tolist())

    metadata = {
        "total_predictions": len(predictions),
        "avg_confidence": float(np.mean(confidences)),
        "low_confidence_count": sum(
            1 for c in confidences if c < config.confidence_threshold
        ),
        "confidence_threshold": config.confidence_threshold,
    }

    logger.info(f"Generated {len(predictions)} batch predictions")

    batch_predictions = {
        "predictions": predictions,
        "confidences": confidences,
    }
    return batch_predictions, metadata


@node(
    inputs=[
        catalog.dummy_batch,
        catalog.production_model,
        catalog.real_time_prediction_config,
        catalog.inference_device,
    ],
    outputs=[
        catalog.real_time_predictions,
        catalog.real_time_prediction_metadata,
    ],
    description="Real-time digit prediction endpoint",
)
def digit_predictions(
    input_images, production_model, config: RealTimePredictionConfig, device
) -> tuple[dict[str, Any], dict]:
    """Classify new handwritten digits in real-time."""

    production_model.to(device)
    production_model.eval()

    # Preprocess input images
    processed_images = input_images.float() / 255.0

    predictions = []
    confidences = []
    all_probabilities = []

    with torch.no_grad():
        processed_images = processed_images.to(device)
        outputs = production_model(processed_images)
        probabilities = torch.softmax(outputs, dim=1)
        predicted_classes = torch.argmax(probabilities, dim=1)
        max_confidences = torch.max(probabilities, dim=1)[0]

        predictions = predicted_classes.cpu().numpy().tolist()
        confidences = max_confidences.cpu().numpy().tolist()

        if config.return_probabilities:
            all_probabilities = probabilities.cpu().numpy().tolist()

    avg_confidence = float(np.mean(confidences))
    metadata = {
        "prediction_count": len(predictions),
        "avg_confidence": avg_confidence,
        "high_confidence_predictions": sum(
            1 for c in confidences if c >= config.confidence_threshold
        ),
        "confidence_threshold": config.confidence_threshold,
    }

    result = {"predictions": predictions, "confidences": confidences}

    if config.return_probabilities:
        result["probabilities"] = all_probabilities

    if avg_confidence < config.confidence_threshold:
        logger.warning(
            f"Average confidence {avg_confidence:.2f} below threshold {config.confidence_threshold}"
        )

    return result, metadata
