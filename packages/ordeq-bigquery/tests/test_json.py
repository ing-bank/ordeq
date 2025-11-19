from unittest.mock import MagicMock

import pytest
from ordeq import IOException
from ordeq_bigquery.json import BigQueryJSON


def test_load_returns_list_of_dicts() -> None:
    bq_json = BigQueryJSON(
        query="SELECT * FROM test_table",
        table_id="test_table",
        client=MagicMock(),
    )
    mock_job = MagicMock()
    mock_job.result.return_value = [{"a": 1}, {"b": 2}]
    bq_json.client.query.return_value = mock_job

    result = bq_json.load()
    assert result == [{"a": 1}, {"b": 2}]


def test_save_inserts_rows_successfully() -> None:
    bq_json = BigQueryJSON(table_id="test_table", client=MagicMock())
    bq_json.client.insert_rows_json.return_value = []
    data = {"field": "value"}
    bq_json.save(data)
    bq_json.client.insert_rows_json.assert_called_once_with(
        table="test_table", json_rows=data
    )


def test_save_raises_on_insert_error() -> None:
    bq_json = BigQueryJSON(table_id="test_table", client=MagicMock())
    bq_json.client.insert_rows_json.return_value = ["error"]
    data = {"field": "value"}
    with pytest.raises(IOException):
        bq_json.save(data)


def test_save_raises_not_implemented_when_no_query() -> None:
    bq_json = BigQueryJSON(table_id="test_table", client=MagicMock())
    with pytest.raises(IOException):
        bq_json.load()
