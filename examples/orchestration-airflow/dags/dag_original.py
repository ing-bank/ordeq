from collections.abc import Mapping

import pendulum
import requests
from airflow.sdk import ObjectStoragePath, dag, task

API = "https://air-quality-api.open-meteo.com/v1/air-quality"

aq_fields = {
    "pm10": "float64",
    "pm2_5": "float64",
    "carbon_monoxide": "float64",
    "nitrogen_dioxide": "float64",
    "sulphur_dioxide": "float64",
    "ozone": "float64",
    "european_aqi": "float64",
    "us_aqi": "float64",
}
base = ObjectStoragePath("s3://aws_default@airflow-tutorial-data/")


@dag(
    schedule=None,
    start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
    catchup=False,
    tags=["example"],
)
def tutorial_objectstorage():
    """
    ### Object Storage Tutorial Documentation
    This is a tutorial DAG to showcase the usage of the Object Storage API.
    Documentation that goes along with the Airflow Object Storage tutorial is
    located
    [here](https://airflow.apache.org/docs/apache-airflow/stable/tutorial/objectstorage.html)
    """

    @task
    def get_air_quality_data(**kwargs) -> ObjectStoragePath:
        """
        #### Get Air Quality Data
        This task gets air quality data from the Finnish Meteorological Institute's
        open data API. The data is saved as parquet.
        """
        import pandas as pd

        logical_date = kwargs["logical_date"]

        latitude = 28.6139
        longitude = 77.2090

        params: Mapping[str, str | float] = {
            "latitude": latitude,
            "longitude": longitude,
            "hourly": ",".join(aq_fields.keys()),
            "timezone": "UTC",
        }

        response = requests.get(API, params=params)
        response.raise_for_status()

        data = response.json()
        hourly_data = data.get("hourly", {})

        df = pd.DataFrame(hourly_data)

        df["time"] = pd.to_datetime(df["time"])

        # ensure the bucket exists
        base.mkdir(exist_ok=True)

        formatted_date = logical_date.format("YYYYMMDD")
        path = base / f"air_quality_{formatted_date}.parquet"

        with path.open("wb") as file:
            df.to_parquet(file)
        return path

    @task
    def analyze(path: ObjectStoragePath):
        """
        #### Analyze
        This task analyzes the air quality data, prints the results
        """
        import duckdb

        conn = duckdb.connect(database=":memory:")
        conn.register_filesystem(path.fs)
        s3_path = path.path
        conn.execute(
            f"CREATE OR REPLACE TABLE airquality_urban AS SELECT * FROM read_parquet('{path.protocol}://{s3_path}')"
        )

        df2 = conn.execute("SELECT * FROM airquality_urban").fetchdf()

        print(df2.head())

    obj_path = get_air_quality_data()
    analyze(obj_path)


tutorial_objectstorage()
