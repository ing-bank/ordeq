import duckdb
import pandas as pd
from ordeq import node

from air_quality_insights import catalog


@node(inputs=catalog.air_quality_json, outputs=catalog.air_quality_data)
def ingest(air_quality_data: dict) -> duckdb.DuckDBPyRelation:
    current_data = air_quality_data.get("current", {})
    df = pd.DataFrame(current_data, index=["time"])
    df["date"] = df["time"].astype("datetime64[ns]")
    return duckdb.from_df(df)


@node(
    inputs=[catalog.air_quality_data], outputs=[catalog.air_quality_insights]
)
def aggregate(air_quality: duckdb.DuckDBPyRelation) -> duckdb.DuckDBPyRelation:
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
