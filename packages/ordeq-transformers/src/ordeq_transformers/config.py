from dataclasses import dataclass
from typing import Optional

@dataclass
class ModelConfig:
    """Configuration for the embedding model."""
    model_name: str = "bert-base-uncased"
    max_length: int = 128
    normalize_embeddings: bool = True
    device: str = "cpu"  # Enforce CPU-only as requested
