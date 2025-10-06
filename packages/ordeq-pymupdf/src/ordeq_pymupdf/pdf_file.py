from dataclasses import dataclass
from pathlib import Path

import pymupdf
from ordeq import IO


@dataclass(frozen=True, kw_only=True)
class PymupdfFile(IO[pymupdf.Document]):
    """IO to load from and save PDF files using Pymupdf.

    Example usage:

    ```pycon
    >>> from pathlib import Path
    >>> from ordeq_pymupdf import PymupdfFile
    >>> MyPDF = PymupdfFile(
    ...     path=Path("path/to.index")
    ... )

    ```

    """

    path: Path

    def load(self) -> pymupdf.Document:
        """Read a PDF file and open the pymypdf Document.

        Returns:
            `pymupdf` Document
        """
        return pymupdf.open(self.path)

    def save(self, document: pymupdf.Document) -> None:
        """Save a pymypdf Document to a file.

        Args:
            document: document to save
        """
        document.save(self.path)
