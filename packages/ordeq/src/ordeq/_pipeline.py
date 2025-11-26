from collections.abc import Callable
from typing import Any

from ordeq._io import IO, AnyIO, Input, Output
from ordeq._resolve import Runnable
from ordeq._runner import run
from ordeq.preview import preview


def pipeline(
    *runnables: Runnable,
    inputs: list[Input],
    outputs: list[Output],
    **run_kwargs: Any,
) -> Callable:
    """Create a pipeline from a runnable with specified inputs and outputs.

    Args:
        runnables: The runnables (nodes, modules, or packages) that make
            up the pipeline.
        inputs: The IO objects representing the inputs to the pipeline.
        outputs: The IO objects representing the outputs from the pipeline.
        run_kwargs: Additional keyword arguments to pass to the `run` function.

    Returns:
        A new callable that represents the pipeline with the specified
        inputs and outputs.
    """

    preview(
        "The pipeline function is experimental and may change in "
        "future releases."
    )

    def runner(*args):
        if len(args) != len(inputs):
            raise ValueError(
                f"Expected {len(inputs)} inputs, but got {len(args)}."
            )

        input_ios: dict[AnyIO, Input] = {
            io: Input(value) for io, value in zip(inputs, args, strict=True)
        }
        output_ios: dict[AnyIO, IO] = {io: IO().retain() for io in outputs}

        run(*runnables, io={**input_ios, **output_ios}, **run_kwargs)  # type: ignore[dict-item]

        output_values = [io.load() for io in output_ios.values()]

        if len(output_values) == 1:
            return output_values[0]
        return tuple(output_values)

    return runner
