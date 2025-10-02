from dataclasses import dataclass, field

import duckdb
from ordeq import IO


@dataclass(frozen=True)
class DuckDBView(IO[duckdb.DuckDBPyRelation]):
    """IO to load and save a DuckDB view.

    Example:

    ```python
    >>> import duckdb
    >>> from ordeq_duckdb import DuckDBView
    >>> connection = duckdb.connect(":memory:")
    >>> view = DuckDBView(
    ...     view="fruits",
    ...     connection=connection
    ... )
    >>> data = connection.values([1, "apples", "red"])
    >>> view.save(data)
    >>> view.load()
    ┌───────┬─────────┬─────────┐
    │ col0  │  col1   │  col2   │
    │ int32 │ varchar │ varchar │
    ├───────┼─────────┼─────────┤
    │     1 │ apples  │ red     │
    └───────┴─────────┴─────────┘
    <BLANKLINE>

    ```

    By default, the view will be replaced if it already exists.
    To change this, pass `replace=False` to the `save` method:

    ```python
    >>> view = view.with_save_options(replace=False)
    >>> view.save(data) # doctest: +SKIP
    IOException('Failed to save DuckDBView(view='fruits', ...

    ```

    Example in a node:

    ```python
    >>> from ordeq import node
    >>> from ordeq_duckdb import DuckDBTable
    >>> import duckdb
    >>> connection = duckdb.connect(":memory:")
    >>> fruits = DuckDBTable(
    ...     table="fruits",
    ...     connection=connection,
    ... )
    >>> fruits_filtered = DuckDBView(
    ...     view="fruits_filtered",
    ...     connection=connection,
    ... )
    >>> @node(inputs=fruits, outputs=fruits_filtered)
    ... def filter_fruits(
    ...     fruits: duckdb.DuckDBPyRelation
    ... ) -> duckdb.DuckDBPyRelation:
    ...     return fruits.filter("color = 'red'")

    ```

    """

    view: str
    connection: duckdb.DuckDBPyConnection | None = field(
        default_factory=duckdb.connect
    )

    def load(self) -> duckdb.DuckDBPyRelation:
        """Loads a DuckDB view.

        Returns:
            The DuckDB view.
        """

        return duckdb.view(self.view, connection=self.connection)

    def save(
        self, relation: duckdb.DuckDBPyRelation, replace: bool = True
    ) -> None:
        """Saves a DuckDB relation to a DuckDB view.

        Args:
            relation: The DuckDB relation to save.
            replace: Whether to replace the view if it already exists.
        """

        relation.create_view(self.view, replace=replace)
