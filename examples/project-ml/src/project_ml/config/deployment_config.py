from dataclasses import dataclass


@dataclass
class DeploymentConfig:
    """Configuration for model deployment."""

    accuracy_threshold: float = 0.90
    custom_model_name: str | None = (
        None  # Allow users to specify a specific model to deploy
    )
    force_deploy: bool = False  # Allow users to bypass accuracy threshold
