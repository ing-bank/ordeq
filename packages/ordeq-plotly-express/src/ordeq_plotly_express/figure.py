import os
from dataclasses import dataclass

import plotly.graph_objects as go
from ordeq import Output
from ordeq.types import PathLike


@dataclass(frozen=True, kw_only=True)
class PlotlyExpressFigure(Output[go.Figure]):
    """IO to save Plotly Express Figures.

    Example usage:

    ```pycon
    >>> from pathlib import Path
    >>> from ordeq_plotly_express import PlotlyExpressFigure
    >>> my_figure = PlotlyExpressFigure(
    ...     path=Path("path/figure.html")
    ... )

    ```

    Args:
        path: output file path
    """

    path: PathLike

    def save(self, fig: go.Figure) -> None:
        ext = os.path.splitext(str(self.path))[1][1:]  # noqa: PTH122
        if ext == "html":
            fig.write_html(str(self.path))
        elif ext == "json":
            fig.write_json(str(self.path))
        elif ext in {"png", "svg", "pdf"}:
            fig.write_image(str(self.path), format=ext)
        else:
            raise ValueError(f"Unsupported file extension: {ext}")
