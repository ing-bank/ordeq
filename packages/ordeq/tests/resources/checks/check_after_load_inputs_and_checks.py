from typing import Any

import pandas as pd
from ordeq import IO, node, run
from ordeq_common import Literal
from ordeq_viz import viz

txs = IO[Any]()
txs_agg = IO[Any]()
threshold = Literal(100)


@node(inputs=[txs_agg, threshold], checks=txs_agg)
def perform_check(txs_agg: pd.DataFrame, t: int) -> None:
    assert txs_agg.count() > t


@node(inputs=txs, outputs=txs_agg)
def agg_txs(txs: pd.DataFrame) -> pd.DataFrame:
    return txs.groupBy(...).agg(...)


if __name__ == "__main__":
    print(viz(__name__, fmt="mermaid"))
    run(__name__)
