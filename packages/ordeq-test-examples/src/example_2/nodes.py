from example_2.catalog import TestInput2, TestOutput2
from ordeq import node


@node(inputs=[TestInput2], outputs=[TestOutput2])
def transform_input_2(input_data: str) -> str:
    """A simple node that transforms input data.

    Args:
        input_data: Input data as a string.

    Returns:
        The transformed input data.
    """
    return input_data.strip()
