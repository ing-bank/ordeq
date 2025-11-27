from typing import Any

from ordeq._io import IO, AnyIO, Input, Output
from ordeq._resolve import Runnable
from ordeq._runner import run
from ordeq.preview import preview


class Pipeline:
    def __init__(
        self,
        *runnables: Runnable,
        inputs: list[Input],
        outputs: list[Output],
        run_kwargs: dict[str, Any] | None = None,
    ) -> None:
        self.runnables = runnables
        self.inputs = inputs
        self.outputs = outputs
        self.run_kwargs = run_kwargs or {}

    def __call__(self, *args) -> Any:
        if len(args) != len(self.inputs):
            raise ValueError(
                f"Expected {len(self.inputs)} inputs, but got {len(args)}."
            )

        input_ios: dict[AnyIO, Input] = {
            io: Input(value)
            for io, value in zip(self.inputs, args, strict=True)
        }
        output_ios: dict[AnyIO, IO] = {
            io: IO().retain() for io in self.outputs
        }

        run(*self.runnables, io={**input_ios, **output_ios}, **self.run_kwargs)  # type: ignore[dict-item]

        output_values = [io.load() for io in output_ios.values()]

        if len(output_values) == 1:
            return output_values[0]
        return tuple(output_values)


def pipeline(
    *runnables: Runnable,
    inputs: list[Input],
    outputs: list[Output],
    **run_kwargs: Any,
) -> Pipeline:
    """Create a pipeline from a runnable with specified inputs and outputs.

    Args:
        runnables: The runnables (nodes, modules, or packages) that make
            up the pipeline.
        inputs: The IO objects representing the inputs to the pipeline.
        outputs: The IO objects representing the outputs from the pipeline.
        run_kwargs: Additional keyword arguments to pass to the `run` function.

    Returns:
        A new callable Pipeline
    """

    preview(
        "The pipeline function is experimental and may change in "
        "future releases."
    )

    return Pipeline(
        *runnables, inputs=inputs, outputs=outputs, run_kwargs=run_kwargs
    )
