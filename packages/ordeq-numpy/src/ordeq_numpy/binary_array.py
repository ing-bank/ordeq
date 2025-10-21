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

    def load(self) -> np.ndarray:
        with self.path.open("rb") as fh:
            return np.load(fh)

    def save(self, array: np.ndarray) -> None:
        with self.path.open("wb") as fh:
            np.save(fh, array)
