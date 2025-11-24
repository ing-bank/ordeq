from typing import Any

import pandas as pd
from ordeq import IO, Input, node, run
from ordeq_viz import viz

txs = Input(
    pd.DataFrame({
        "id": [1, 2, 3],
        "amount": [100, 200, 300],
        "to": ["me", "me", "you"],
        "country": ["NL", "BE", "US"],
    })
)
txs_agg = IO[Any]()
threshold = Input(100)


@node(inputs=[txs_agg, threshold], checks=txs_agg)
def perform_check(txs_agg: pd.DataFrame, t: int) -> None:
    assert (txs_agg.count() < t).all()


@node(inputs=txs, outputs=txs_agg)
def agg_txs(txs: pd.DataFrame) -> pd.DataFrame:
    return txs.groupby("country").agg({"amount": "sum"})


if __name__ == "__main__":
    print(viz(__name__, fmt="mermaid"))
    run(__name__)
