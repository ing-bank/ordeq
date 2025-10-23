from dataclasses import dataclass
from typing import Any

import numpy as np
from ordeq import IO
from ordeq.types import PathLike


@dataclass(frozen=True, kw_only=True)
class NumpyBinary(IO[np.ndarray]):
    """IO to load from and save binary numpy arrays.

    Example usage:

    ```pycon
    >>> from pathlib import Path
    >>> from ordeq_numpy import NumpyBinary
    >>> MyArray = NumpyBinary(
    ...     path=Path("path/to.npy")
    ... )

    ```

    """

    path: PathLike

    def load(self, **load_options: Any) -> np.ndarray:
        """Load numpy array with optional parameters.

        Args:
            **load_options: Arguments passed to np.load()
                (e.g., mmap_mode, allow_pickle, max_header_size)

        Returns:
            Numpy array
        """
        with self.path.open("rb") as fh:
            return np.load(fh, **load_options)

    def save(self, array: np.ndarray) -> None:
        with self.path.open("wb") as fh:
            np.save(fh, array)
