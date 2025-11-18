from collections.abc import Iterable
from dataclasses import dataclass
from typing import TypeVar

from ordeq import IO

T = TypeVar("T")


@dataclass(frozen=True)
class _Iterate(IO[Iterable[T]]):
    ios: tuple[IO[T], ...]

    def load(self) -> Iterable[T]:
        for io in self.ios:
            yield io.load()

    def save(self, data: Iterable[T]) -> None:
        for io, contents in zip(self.ios, data, strict=True):
            io.save(contents)


def Iterate(*ios: IO[T]) -> _Iterate[T]:
    """IO for loading and saving iteratively. This can be useful when
    processing multiple IOs using the same node, while only requiring
    to have one of them in memory at the same time.

    Examples:

    The load function returns a generator:

    ```pycon
    >>> from pathlib import Path
    >>> from ordeq_files import Text, JSON
    >>> from ordeq_common import Iterate
    >>> paths = [Path("hello.txt"), Path("world.txt")]
    >>> text_ios = Iterate(*[Text(path=path) for path in paths])
    >>> text_ios.load()  # doctest: +SKIP
    <generator object Iterate._load at 0x104946f60>
    ```

    The load function returns the contents of the files in this case:

    ```pycon
    >>> list(text_ios.load())  # doctest: +SKIP
    ['hello', 'world']
    ```

    By iterating over the contents, each file will be loaded and saved
    without the need to keep multiple files in memory at the same time:

    ```pycon
    >>> for idx, content in enumerate(text_ios.load()):   # doctest: +SKIP
    ...    JSON(
    ...        path=paths[idx].with_suffix(".json")
    ...    ).save({"content": content})

    ```

    We can achieve the same by passing a generator to the `Iterate.save`
    method:

    ```pycon
    >>> json_dataset = Iterate(
    ...     *[
    ...         JSON(path=path.with_suffix(".json"))
    ...         for path in paths
    ...     ]
    ... )
    >>> json_dataset.save(
    ...    ({"content": content} for content in text_ios.load())
    ... )   # doctest: +SKIP
    >>> from collections.abc import Iterable
    >>> def generate_json_contents(
    ...     contents: Iterable[str]
    ... ) -> Iterable[dict[str, str]]:
    ...     for content in contents:
    ...         yield {"content": content}
    >>> json_dataset.save(generate_json_contents(text_ios.load()))   # doctest: +SKIP

    ```

    Returns:
        _Iterate

    """  # noqa: E501 (line too long)

    return _Iterate(ios=tuple(ios))
