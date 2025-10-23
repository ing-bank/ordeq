from dataclasses import dataclass


@dataclass
class ModelEvaluationConfig:
    """Configuration for model evaluation."""

    batch_size: int = 64
    accuracy_threshold: float = 0.90
