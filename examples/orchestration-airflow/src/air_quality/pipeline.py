import duckdb
import pandas as pd
from ordeq import node

from air_quality import catalog


@node(inputs=catalog.air_quality_json, outputs=catalog.air_quality_data)
def ingest(air_quality: dict) -> duckdb.DuckDBPyRelation:
    data = air_quality.get("current")
    df = pd.DataFrame(data, index=[0])
    df["date"] = df["time"].astype("datetime64[ns]")
    return duckdb.from_df(df)


@node(inputs=catalog.air_quality_data, outputs=catalog.air_quality_insights)
def aggregate(air_quality: duckdb.DuckDBPyRelation) -> duckdb.DuckDBPyRelation:
    return air_quality.aggregate(
        "DATE(time) AS date"
        "AVG(pm2_5) AS avg_pm2_5"
        "AVG(european_aqi) AS avg_european_aqi"
        "AVG(us_aqi) AS avg_us_aqi"
    ).select("date, avg_pm2_5, avg_european_aqi, avg_us_aqi")
