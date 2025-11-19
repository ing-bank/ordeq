from dataclasses import dataclass
from typing import Any

import pandas as pd
from google.cloud import bigquery
from ordeq import IO


@dataclass(frozen=True, kw_only=True)
class BigQueryPandas(IO[pd.DataFrame]):
    """BigQueryTable extension for loading and saving pandas DataFrames.

    Example:
        >>> from ordeq_bigquery import BigQueryPandas
        >>> from google.cloud import bigquery
        >>>
        >>> client = bigquery.Client()
        >>> table = BigQueryPandas(
        ...     table_id="project.dataset.table", client=client
        ... )  # doctest: +SKIP
        >>> df = table.load()  # doctest: +SKIP
        >>> table.save(df)  # doctest: +SKIP
    """

    table_id: str | bigquery.Table
    client: bigquery.Client

    def load(self, **load_options: Any) -> pd.DataFrame:
        """Loads the BigQuery table as a pandas DataFrame.

        Args:
            **load_options: Additional options passed to `to_dataframe`.

        Returns:
            A pandas DataFrame containing the table data.

        Example:
            >>> from ordeq_bigquery import BigQueryPandas
            >>> from google.cloud import bigquery
            >>>
            >>> client = bigquery.Client()
            >>> table = BigQueryPandas(
            ...     table_id="project.dataset.table", client=client
            ... )  # doctest: +SKIP
            >>> df = table.load()  # doctest: +SKIP
        """
        table = self.client.get_table(self.table_id)
        return self.client.list_rows(table).to_dataframe(**load_options)

    def save(self, df: pd.DataFrame, **save_options: Any) -> None:
        """Saves a pandas DataFrame to the BigQuery table.

        Args:
            df: The pandas DataFrame to save.
            **save_options: Options passed to `load_table_from_dataframe`.

        Example:
            >>> import pandas as pd
            >>> from ordeq_bigquery import BigQueryPandas
            >>>
            >>> from google.cloud import bigquery
            >>> client = bigquery.Client()
            >>> table = BigQueryPandas(
            ...     table_id="project.dataset.table", client=client
            ... )  # doctest: +SKIP
            >>> df = pd.DataFrame({"a": [1, 2], "b": [3, 4]})
            >>> table.save(df)  # doctest: +SKIP
        """
        self.client.load_table_from_dataframe(
            dataframe=df, destination=self.table_id, **save_options
        ).result()
