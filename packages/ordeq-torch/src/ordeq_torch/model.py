from dataclasses import dataclass
from typing import Any

import torch.nn
from ordeq import IO
from ordeq.types import PathLike


@dataclass(frozen=True, kw_only=True)
class TorchModel(IO):
    """IO class for reading and writing PyTorch models using state
    dictionaries.

    This class provides safe loading by using `torch.load` with
    `weights_only=True` and requires the model class to be specified for
    instantiation.

    Example usage:

    ```pycon
    >>> from pathlib import Path
    >>> import torch.nn as nn
    >>> from ordeq_torch import TorchModel
    >>>
    >>> # Define a simple model class
    >>> class SimpleModel(nn.Module):
    ...     def __init__(self, input_size, hidden_size):
    ...         super().__init__()
    ...         self.linear = nn.Linear(input_size, hidden_size)
    ...
    >>> model_path = Path("model_state.pth")
    >>> io = TorchModel(
    ...     path=model_path,
    ...     model_class=SimpleModel,
    ...     model_args=(10, 5)
    ... )
    >>> # Load a model
    >>> model = io.load()  # doctest: +SKIP
    >>> # Save a model's state dict
    >>> io.save(model)  # doctest: +SKIP

    ```
    """

    path: PathLike
    model_class: type[torch.nn.Module] | None = None
    model_args: tuple[Any, ...] = ()
    model_kwargs: dict[str, Any] = None

    def load(self, **load_options: Any) -> torch.nn.Module:
        """Load a PyTorch model by instantiating the model class and loading
        its state dict.

        Creates a new instance of the specified model class using the provided
        arguments and kwargs, then loads the state dictionary from the file
        and sets the model to evaluation mode.

        Args:
            **load_options: Additional options to pass to `torch.load`.

        Returns:
            The instantiated PyTorch model with loaded weights in
            evaluation mode.

        Raises:
            ValueError: If model_class is None.
        """
        if self.model_class is None:
            raise ValueError("model_class must be provided to load a model.")

        model = self.model_class(*self.model_args, **(self.model_kwargs or {}))
        state_dict = torch.load(self.path, weights_only=True, **load_options)
        model.load_state_dict(state_dict)
        model.eval()
        return model

    def save(self, model: torch.nn.Module, **save_options: Any) -> None:
        """Save a PyTorch model's state dictionary to the specified path.

        Extracts the state dictionary from the model and saves it to the file.
        This approach provides safer loading compared to saving the entire
        model object.

        Args:
            model: The PyTorch model whose state dict should be saved.
            **save_options: Additional options to pass to `torch.save`.
        """
        torch.save(model.state_dict(), self.path, **save_options)
