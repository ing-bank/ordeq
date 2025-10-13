from dataclasses import dataclass, field
from typing import Literal

import duckdb
from ordeq import IO


@dataclass(frozen=True)
class DuckDBTable(IO[duckdb.DuckDBPyRelation]):
    """IO to load from and save to a DuckDB table.

    Example:

    ```pycon
    >>> import duckdb
    >>> from ordeq_duckdb import DuckDBTable
    >>> connection = duckdb.connect(":memory:")
    >>> table = DuckDBTable(
    ...     table="my_table",
    ...     connection=connection
    ... )
    >>> table.save(
    ...     connection.values([123, "abc"])
    ... )
    >>> connection.sql("SELECT * FROM my_table").show()
    ┌───────┬─────────┐
    │ col0  │  col1   │
    │ int32 │ varchar │
    ├───────┼─────────┤
    │   123 │ abc     │
    └───────┴─────────┘
    <BLANKLINE>

    ```

    Example in a node:

    ```pycon
    >>> from ordeq import node, run
    >>> from pathlib import Path
    >>> connection = duckdb.connect(":memory:")
    >>> table = DuckDBTable(
    ...     table="my_data",
    ...     connection=connection,
    ... )
    >>> @node(outputs=table)
    ... def convert_to_duckdb_relation() -> duckdb.DuckDBPyRelation:
    ...     return connection.values([2, "b"])
    >>> result = run(convert_to_duckdb_relation)
    >>> connection.table("my_data").show()
    ┌───────┬─────────┐
    │ col0  │  col1   │
    │ int32 │ varchar │
    ├───────┼─────────┤
    │     2 │ b       │
    └───────┴─────────┘
    <BLANKLINE>

    ```

    """

    table: str
    connection: duckdb.DuckDBPyConnection = field(
        default_factory=duckdb.connect
    )

    def load(self) -> duckdb.DuckDBPyRelation:
        """Load the DuckDB table into a DuckDB relation.

        Returns:
            A relation representing the loaded table.
        """

        return duckdb.table(self.table, connection=self.connection)

    def save(
        self,
        relation: duckdb.DuckDBPyRelation,
        mode: Literal["create", "insert"] = "create",
    ) -> None:
        """Save a relation to the DuckDB table.

        Args:
            relation: The relation to save.
            mode: The save mode.
                "create" will create the table,
                "insert" will insert into the table if it exists,
                or create it if it doesn't.

        Raises:
            CatalogException: If the table already exists and mode is "create".

        """

        if mode == "create":
            relation.create(self.table)
        elif mode == "insert":
            try:
                relation.create(self.table)
            except duckdb.CatalogException as e:
                if "already exists" in e.args[0]:
                    relation.insert_into(self.table)
                else:
                    raise
