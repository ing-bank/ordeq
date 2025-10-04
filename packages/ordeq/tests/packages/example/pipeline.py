from ordeq import node

from .catalog import (  # ty: ignore[unresolved-import]
    Hello,
    TestInput,
    TestOutput,
    World,
)


@node(inputs=[TestInput], outputs=[TestOutput])
def transform_input(input_data: str) -> str:
    """A simple node that transforms input data.

    Args:
        input_data: Input data as a string.

    Returns:
        The transformed input data.
    """
    return input_data.strip()


@node(inputs=[Hello], outputs=[World])
def transform_mock_input(input_data: str) -> str:
    """A mock node that transforms Hello input to World output.

    Args:
        input_data: Input data as a string.

    Returns:
        The transformed input data, replacing "Hello" with "World".
    """
    return input_data.replace("Hello", "World")
