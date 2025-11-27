from dataclasses import dataclass


@dataclass
class ModelConfig:
    """Configuration for model architecture and training."""

    # Architecture parameters
    conv1_channels: int = 32  # Reduced complexity
    conv2_channels: int = 64
    conv3_channels: int = 128
    dropout1_rate: float = 0.1  # Reduced dropout
    dropout2_rate: float = 0.2
    hidden_size: int = 256
    use_batch_norm: bool = True


@dataclass
class ModelTrainingConfig:
    # Training parameters
    batch_size: int = 64  # Smaller batch size for better generalization
    learning_rate: float = 0.001  # Reduced learning rate
    epochs: int = 1  # 30  # Increased epochs
    optimizer_type: str = "adam"  # Changed to Adam
    momentum: float = 0.9
    weight_decay: float = 1e-5  # Reduced weight decay

    # Learning rate scheduling
    use_lr_scheduler: bool = True
    lr_step_size: int = 10
    lr_gamma: float = 0.1

    # Early stopping
    use_early_stopping: bool = True
    patience: int = 7
    min_delta: float = 0.001

    # Data augmentation - Research proven techniques
    use_data_augmentation: bool = True
    rotation_degrees: float = 15.0  # Increased from 10
    translation_pixels: float = 0.1  # New parameter
    scale_range_min: float = 0.9  # Split tuple into two floats
    scale_range_max: float = 1.1  # Split tuple into two floats
