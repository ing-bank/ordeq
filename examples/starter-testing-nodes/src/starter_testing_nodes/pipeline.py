from collections.abc import Iterable

from ordeq import node

from starter_testing_nodes import catalog


@node(inputs=catalog.names, outputs=catalog.greetings)
def greet(rows: Iterable[tuple[str, ...]]) -> list[list[str]]:
    """Returns a greeting for each person."""
    return [[f"Hello, {row[0]}!"] for row in rows]
