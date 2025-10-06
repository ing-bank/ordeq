import os
from typing import Any, Literal, get_args

import altair as alt
from ordeq import Output
from ordeq.types import PathLike

Formats = Literal["json", "html", "png", "svg", "pdf"]


class AltairChart(Output[alt.Chart]):
    """IO to save altair Charts.

    Example usage:

    ```pycon
    >>> from pathlib import Path
    >>> from ordeq_altair import AltairChart
    >>> my_chart = AltairChart(
    ...     path=Path("path/figure.pdf")
    ... )

    ```

    """

    path: PathLike
    _fmt: Formats

    def __init__(self, path: PathLike):
        super().__init__()
        self.path = path
        fmt = os.path.splitext(str(self.path))[1][1:]  # noqa: PTH122
        if fmt not in get_args(Formats):
            raise ValueError(
                f"Path extension must be one of {get_args(Formats)}"
            )
        self._fmt = fmt  # type: ignore[assignment]

    def save(self, chart: alt.Chart, **save_options: Any) -> None:
        """Saves the Altair chart to a specified path in HTML format.

        Args:
            chart: The Altair chart to save.
            **save_options: Additional options to pass to the `save` method.
        """
        with self.path.open(mode="wb") as fh:
            chart.save(fh, format=self._fmt, **save_options)
