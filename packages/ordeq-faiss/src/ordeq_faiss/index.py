from dataclasses import dataclass
from pathlib import Path

import faiss
from ordeq.framework.io import IO


@dataclass(frozen=True, kw_only=True)
class FaissIndex(IO[faiss.Index]):
    """IO to load from and save index data using Faiss. Calls
    `faiss.read_index` and `faiss.write_index` under the hood.

    Example usage:

    ```pycon
    >>> from pathlib import Path
    >>> from ordeq_faiss import FaissIndex
    >>> my_index = FaissIndex(
    ...     path=Path("path/to.index")
    ... )

    ```

    """

    path: Path

    def load(self) -> faiss.Index:
        return faiss.read_index(str(self.path))

    def save(self, index: faiss.Index) -> None:
        faiss.write_index(index, str(self.path))
