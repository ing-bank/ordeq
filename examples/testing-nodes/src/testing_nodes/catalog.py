from ordeq_args import CommandLineArg
from ordeq_polars import PolarsEagerParquet

date = CommandLineArg("--date", type=str)
txs = PolarsEagerParquet(path="s3://bucket/txs.parquet")
clients = PolarsEagerParquet(path="s3://bucket/clients.parquet")
txs_and_clients = PolarsEagerParquet(
    path="s3://bucket/txs_and_clients.parquet"
)
aggregated_txs = PolarsEagerParquet(path="s3://bucket/aggregated-txs.parquet")
