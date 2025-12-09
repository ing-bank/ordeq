from ordeq_duckdb import DuckDBParquet
from ordeq_requests import ResponseJSON

from air_quality.paths import DATA_DIRECTORY

air_quality_json = ResponseJSON(
    url="https://air-quality-api.open-meteo.com/v1/air-quality"
).with_load_options(
    params={
        "latitude": 28.6139,
        "longitude": 77.2090,
        "current": ",".join({
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

air_quality_data = (
    DuckDBParquet(path=str(DATA_DIRECTORY / "air_quality"))
).with_save_options(partition_by=["date"], overwrite=True)

air_quality_insights = DuckDBParquet(
    path=str(DATA_DIRECTORY / "air_quality_insights.parquet")
)
