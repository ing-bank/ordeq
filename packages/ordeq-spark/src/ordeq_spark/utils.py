from pyspark.sql import SparkSession


def get_spark_session() -> SparkSession:
    """Helper to get the SparkSession

    Returns:
        the spark session object

    Raises:
        RuntimeError: when the spark session is not active
    """
    session = SparkSession.getActiveSession()
    if session is None:
        raise RuntimeError("Spark session must be active.")
    return session
