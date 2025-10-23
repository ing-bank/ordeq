from dataclasses import dataclass
from typing import Any

import numpy as np
from ordeq import IO
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

    def load(self, **load_options: Any) -> np.ndarray:
        """Load numpy array with optional parameters.

        Args:
            **load_options: Arguments passed to np.loadtxt()
                (e.g., dtype, delimiter, skiprows, max_rows)

        Returns:
            Numpy array
        """
        with self.path.open("r") as fh:
            return np.loadtxt(fh, **load_options)

    def save(self, array: np.ndarray, **save_options: Any) -> None:
        """Save numpy array with optional parameters.

        Args:
            array: The array to save
            **save_options: Arguments passed to np.savetxt()
                (e.g., fmt, delimiter, header, footer)
        """
        with self.path.open("w") as fh:
            np.savetxt(fh, array, **save_options)
