from dataclasses import dataclass

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

    def load(self, mmap_mode: str | None = None) -> np.ndarray:
        """Load numpy array with optional memory mapping.

        Args:
            mmap_mode: Memory-map mode for large arrays:
                - None: Load into RAM (default)
                - 'r': Read-only memory map
                - 'r+': Read-write memory map
                - 'c': Copy-on-write

        Returns:
            Numpy array (memory-mapped if mmap_mode is set)
        """
        with self.path.open("rb") as fh:
            return np.load(fh, allow_pickle=False, mmap_mode=mmap_mode)

    def save(self, array: np.ndarray) -> None:
        with self.path.open("wb") as fh:
            np.save(fh, array)
