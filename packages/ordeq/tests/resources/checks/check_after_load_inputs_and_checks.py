from typing import Any

from ordeq import IO, node, run
from ordeq_common import Literal
from ordeq_viz import viz
from pandas import DataFrame

txs = IO[Any]()
txs_agg = IO[Any]()
threshold = Literal(100)


@node(inputs=[txs_agg, threshold], checks=txs_agg)
def perform_check(txs_agg: DataFrame, t: int) -> None:
    assert txs_agg.count() > t


@node(inputs=txs, outputs=txs_agg)
def agg_txs(txs: DataFrame) -> DataFrame:
    return txs.groupBy(...).agg(...)


if __name__ == "__main__":
    print(viz(__name__, fmt="mermaid"))
    run(__name__)
