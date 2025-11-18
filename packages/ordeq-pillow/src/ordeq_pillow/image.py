from dataclasses import dataclass
from typing import Any

from ordeq import IO
from ordeq.types import PathLike
from PIL import Image


@dataclass
class PillowImage(IO[Image.Image]):
    """IO that loads and saves PIL Image objects to and from disk.

    Example:
    ```pycon
    >>> from ordeq_pillow import PillowImage
    >>> from PIL import Image
    >>> from pathlib import Path
    >>> image = PillowImage(path=Path("example.png"))
    >>> img = Image.new("RGB", (100, 100), color="red")
    >>> image.save(img)
    >>> loaded_img = image.load()
    >>> loaded_img.size
    (100, 100)

    ```
    """

    path: PathLike

    def load(
        self,
        mode: str = "rb",
        formats: list[str] | tuple[str, ...] | None = None,
    ) -> Image.Image:
        with self.path.open(mode=mode) as fp:
            img = Image.open(fp, formats=formats)
            img.load()
            return img

    def save(
        self,
        data: Image.Image,
        mode: str = "wb",
        format: str | None = None,  # noqa: A002
        **save_options: Any,
    ) -> None:
        with self.path.open(mode=mode) as fp:
            data.save(fp, format=format, **save_options)
