import csv
from collections.abc import Iterable
from dataclasses import dataclass
from typing import Any

from ordeq import IO
from ordeq.types import PathLike


@dataclass(frozen=True, kw_only=True)
class CSV(IO[Iterable[Iterable[Any]]]):
    """IO representing a CSV file.

    Example usage:

    ```pycon
    >>> from ordeq_files import CSV
    >>> from pathlib import Path
    >>> computer_sales = CSV(
    ...     path=Path("path/to/computer_sales.csv")
    ... )

    ```

    Example in a node:

    ```pycon
    >>> from ordeq import node
    >>> computer_sales_in_nl = CSV(path=Path("computer_sales_nl.csv"))
    >>> @node(
    ...     inputs=computer_sales,
    ...     outputs=computer_sales_in_nl
    ... )
    ... def filter_computer_sales(computer_sales: list) -> list:
    ...     return [row for row in computer_sales if row[1] == "NL"]

    ```

    Example with a node generator:

    ```pycon
    >>> from pathlib import Path
    >>> from ordeq import node
    >>> from ordeq_files import CSV
    >>> @node(outputs=CSV(path=Path("output.csv")))
    ... def generator():
    ...     yield ["constant", "idx"]
    ...     for idx in range(100):
    ...         yield [1, idx]

    >>> if __name__ == "__main__":
    ...     from ordeq import run
    ...     run(generator)

    ```

    Loading and saving can be configured with additional parameters, e.g:

    ```pycon
    >>> computer_sales.load(quotechar='"', delimiter=',')  # doctest: +SKIP
    >>> computer_sales.with_load_options(dialect='excel').load()  # doctest: +SKIP
    >>> data = [["NL", "2023-10-01", 1000], ["BE", "2023-10-02", 1500]]
    >>> computer_sales.save(data, quoting=csv.QUOTE_MINIMAL)  # doctest: +SKIP

    ```

    Refer to [1] for more details on the available options.

    [1]: https://docs.python.org/3/library/csv.html

    """  # noqa: E501 (line too long)

    path: PathLike

    def load(self, mode="r", **load_options: Any) -> Iterable[Iterable[Any]]:
        with self.path.open(mode=mode) as fh:
            reader = csv.reader(fh, **load_options)
            return list(reader)

    def save(
        self, data: Iterable[Iterable[Any]], mode="w", **save_options: Any
    ) -> None:
        with self.path.open(mode=mode) as fh:
            writer = csv.writer(fh, **save_options)
            writer.writerows(data)
