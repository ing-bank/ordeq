from dataclasses import dataclass
from typing import Any

import torch.nn
from ordeq import IO
from ordeq.types import PathLike


@dataclass(frozen=True, kw_only=True)
class TorchObject(IO[Any]):
    """IO class for reading and writing arbitrary PyTorch objects using pickle.

    This class can load and save any PyTorch-compatible object including
    tensors and Python data structures. It uses PyTorch's native serialization
    which is based on Python's pickle protocol.

    Example usage:

    ```pycon
    >>> from pathlib import Path
    >>> import torch
    >>> from ordeq_torch import TorchObject
    >>>
    >>> # Save and load a tensor
    >>> tensor_path = Path("tensor.pt")
    >>> io = TorchObject(path=tensor_path)
    >>> tensor = torch.randn(3, 4)
    >>> io.save(tensor)  # doctest: +SKIP
    >>> loaded_tensor = io.load()  # doctest: +SKIP
    >>>
    >>> # Can also save other objects like lists of tensors
    >>> data = [torch.randn(2, 2), {"key": torch.ones(5)}]
    >>> io.save(data)  # doctest: +SKIP

    ```
    """

    path: PathLike

    def load(self, **load_options: Any) -> Any:
        """Load a PyTorch object from the file specified by the path attribute.

        Uses `torch.load` to deserialize the object. The loaded object can be
        a tensor, Python data structure or any other Pickle-compatible object.

        Args:
            **load_options: Additional options to pass to `torch.load`.

        Returns:
            The deserialized PyTorch object.
        """
        return torch.load(self.path, **load_options)

    def save(self, data: Any, **save_options: Any) -> None:
        """Save a PyTorch object to the file specified by the path attribute.

        Serializes any Pickle-compatible object including tensors or
        Python data structures to a file using `torch.save`.

        Args:
            data: The PyTorch object to be saved.
            **save_options: Additional options to pass to `torch.save`.
        """
        torch.save(data, self.path, **save_options)
