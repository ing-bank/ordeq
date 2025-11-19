from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from typing import Any

from google.cloud import bigquery
from ordeq import IO, IOException


@dataclass(frozen=True)
class BigQueryJSON(IO[list[dict]]):
    """IO for loading data using a user provided query and saving data from
    JSON-copmatible data representation.

    Args:
        table_id: BigQuery table identifier
        client: BigQuery client
        query:
    """

    table_id: str | bigquery.Table
    client: bigquery.Client
    query: str | None = None

    def load(self, **query_options) -> list[dict]:
        """Loads query results from BigQuery.

        Args:
            **query_options: Additional options for the query.

        Returns:
            List of rows as dictionaries. Raises typeerror with query is not
            provided.

        Raises:
            TypeError: if query is not provided, i.e. is None

        Example:
            >>> from google.cloud import bigquery
            >>> from ordeq_bigquery import BigQueryJSON
            >>>
            >>> client = bigquery.Client()
            >>> inp = BigQueryJSON(
            ...     query="SELECT * FROM my_table",
            ...     table_id="project.dataset.table",
            ...     client=client,
            ... )  # doctest: +SKIP
            >>> rows = inp.load()  # doctest: +SKIP
        """
        if self.query is None:
            raise TypeError("Loading is only supported if query is provided")
        job = self.client.query(self.query, **query_options)
        return list(job.result())

    def save(self, data: Sequence[Mapping[str, Any]], **save_options) -> None:
        """Saves JSON rows to BigQuery.

        Args:
            data: Dictionary or list of dictionaries to insert.
            **save_options: Additional options for saving.

        Raises:
            IOException: If insertion fails.

        Example:
            >>> from google.cloud import bigquery
            >>> from ordeq_bigquery import BigQueryJSON
            >>>
            >>> client = bigquery.Client()
            >>> out = BigQueryJSON(
            ...     table_id="project.dataset.table", client=client
            ... )  # doctest: +SKIP
            >>> out.save([
            ...     {"col1": "val1"},
            ...     {"col1": "val2"},
            ... ])  # doctest: +SKIP
        """
        errors = self.client.insert_rows_json(
            table=self.table_id, json_rows=data, **save_options
        )
        if errors:
            raise IOException(f"Failed to insert rows: {errors}")
