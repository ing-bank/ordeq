from dataclasses import dataclass


@dataclass
class RealTimePredictionConfig:
    """Configuration for real-time prediction processing."""

    batch_size: int = 10  # Default number of images to process at once
    return_probabilities: bool = (
        False  # Whether to return full probability distribution
    )
    confidence_threshold: float = 0.9  # Higher threshold for real-time predictions
    device: str = "cuda"  # Will fallback to CPU if CUDA not available
