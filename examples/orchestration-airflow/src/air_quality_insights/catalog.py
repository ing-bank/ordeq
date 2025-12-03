from datetime import date
from pathlib import Path

from ordeq import Input
from ordeq_duckdb import DuckDBParquet
from ordeq_pandas import PandasParquet
from ordeq_requests import ResponseJSON

DATA_DIRECTORY = Path(__file__).resolve().parent.parent.parent / "data"

air_quality_json = ResponseJSON(
    url="https://air-quality-api.open-meteo.com/v1/air-quality"
).with_load_options(
    params={
        "latitude": 28.6139,
        "longitude": 77.2090,
        "hourly": ",".join({
            "pm10": "float64",
            "pm2_5": "float64",
            "carbon_monoxide": "float64",
            "nitrogen_dioxide": "float64",
            "sulphur_dioxide": "float64",
            "ozone": "float64",
            "european_aqi": "float64",
            "us_aqi": "float64",
        }),
        "timezone": "UTC",
    }
)

air_quality_path = DATA_DIRECTORY / "air_quality"

air_quality_pandas = (
    PandasParquet(path=air_quality_path).with_save_options(
        partition_cols=["date"]
    )
    @ air_quality_path
)

air_quality_duckdb = (
    DuckDBParquet(path=str(air_quality_path)) @ air_quality_path
)

air_quality_insights = DuckDBParquet(
    path=str(DATA_DIRECTORY / "air_quality_insights.parquet")
)

logical_date = Input(date(2025, 12, 16))
