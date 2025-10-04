from dataclasses import dataclass

import numpy as np
from ordeq.framework.io import IO
from ordeq.types import PathLike


@dataclass(frozen=True, kw_only=True)
class NumpyText(IO[np.ndarray]):
    """IO to load from and save plain text numpy arrays.

    Example usage:

    ```pycon
    >>> from pathlib import Path
    >>> from ordeq_numpy import NumpyText
    >>> MyArray = NumpyText(
    ...     path=Path("path/to.txt")
    ... )

    ```

    """

    path: PathLike

    def load(self) -> np.ndarray:
        with self.path.open("r") as fh:
            return np.loadtxt(fh)

    def save(self, array: np.ndarray) -> None:
        with self.path.open("w") as fh:
            np.savetxt(fh, array)
