from dataclasses import dataclass
from pathlib import Path
from typing import Any

from ordeq import Input
from PIL import Image


@dataclass
class PDF2Image(Input[list[Image.Image]]):
    """Input that loads images from a PDF file.

    Example:
    ```pycon
    >>> from ordeq_pillow import PDF2Image
    >>> from pathlib import Path
    >>> pdf_path = PDF2Image(path=Path("example.pdf"))
    >>> images = pdf_path.load()  # doctest: +SKIP
    >>> len(images)  # doctest: +SKIP
    3  # Number of pages in the PDF
    >>> images[0].size  # doctest: +SKIP
    (612, 792)  # Size of the first page image
    """

    path: Path

    def load(self, **load_options: Any) -> list[Image.Image]:
        import pdf2image  # noqa: PLC0415

        return pdf2image.convert_from_path(self.path, **load_options)
