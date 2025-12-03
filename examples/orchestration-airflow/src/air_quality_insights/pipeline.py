from datetime import date

import duckdb
import pandas as pd
from ordeq import node

from air_quality_insights import catalog


@node(
    inputs=[catalog.air_quality_json, catalog.logical_date],
    outputs=catalog.air_quality_pandas,
)
def get_air_quality_data(
    air_quality: dict, logical_date: date
) -> pd.DataFrame:
    hourly_data = air_quality.get("hourly", {})
    df = pd.DataFrame(hourly_data)
    df["time"] = pd.to_datetime(df["time"])
    df["date"] = logical_date
    return df


@node(
    inputs=[catalog.air_quality_duckdb], outputs=[catalog.air_quality_insights]
)
def analyze(air_quality: duckdb.DuckDBPyRelation) -> duckdb.DuckDBPyRelation:
    daily_stats = air_quality.aggregate(
        """
        DATE(time) AS date,
        AVG(pm2_5) AS avg_pm2_5,
        AVG(european_aqi) AS avg_european_aqi,
        AVG(us_aqi) AS avg_us_aqi
        """
    )
    return daily_stats.select(
        """
        date,
        avg_pm2_5,
        avg_european_aqi,
        avg_us_aqi
        """
    )
