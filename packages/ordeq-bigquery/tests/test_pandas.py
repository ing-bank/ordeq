from unittest.mock import MagicMock

import pandas as pd
import pytest
from ordeq_bigquery.dataframe import BigQueryPandas


class MockRows:
    def to_dataframe(self, **kwargs):
        return pd.DataFrame({"a": [1], "b": [2]})


class MockClient:
    def get_table(self, table_id):
        return MagicMock()

    def load_table_from_dataframe(self, dataframe, destination, **kwargs):
        class Result:
            def result(self):
                return None

        return Result()

    def list_rows(self, table):
        return MockRows()


@pytest.fixture
def bigquery_pandas():
    return BigQueryPandas(
        table_id="project.dataset.table", client=MockClient()
    )


def test_load_returns_dataframe(bigquery_pandas):
    df = bigquery_pandas.load()
    assert isinstance(df, pd.DataFrame)
    assert list(df.columns) == ["a", "b"]


def test_save_calls_load_table_from_dataframe(bigquery_pandas):
    df = pd.DataFrame({"a": [1], "b": [2]})
    mocker = MagicMock()
    mock = mocker.patch.object(
        bigquery_pandas.client, "load_table_from_dataframe", autospec=True
    )
    mock.return_value.result.return_value = None
    bigquery_pandas.save(df)
