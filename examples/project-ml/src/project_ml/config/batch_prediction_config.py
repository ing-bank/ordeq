from dataclasses import dataclass


@dataclass
class BatchPredictionConfig:
    """Configuration for batch prediction processing."""

    batch_size: int = 64
    num_test_images: int = 100  # Number of dummy images for demo
    confidence_threshold: float = 0.8  # Threshold for low confidence warning
    device: str = "cuda"  # Will fallback to CPU if CUDA not available
