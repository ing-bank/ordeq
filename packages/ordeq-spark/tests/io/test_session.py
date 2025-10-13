from unittest.mock import Mock, patch

import pyspark.sql
import pytest
from ordeq import IOException
from ordeq_spark.io.session import SparkSession


def test_it_loads_active_session(spark: pyspark.sql.SparkSession):
    assert SparkSession().load() == spark


@patch("pyspark.sql.SparkSession.getActiveSession")
def test_it_raises_if_no_active_session(getter: Mock):
    getter.return_value = None  # Simulate no active session
    with pytest.raises(IOException, match="Spark session must be active"):
        SparkSession().load()
