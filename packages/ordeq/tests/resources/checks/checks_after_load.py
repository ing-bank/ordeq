from typing import Any

import pandas as pd
from ordeq import IO, node, run
from ordeq_common import Literal
from ordeq_viz import viz

txs = Literal(
    pd.DataFrame({
        "id": [1, 2, 3],
        "amount": [100, 200, 300],
        "to": ["me", "me", "you"],
    })
)
txs_agg = IO[Any]()


@node(inputs=txs, checks=txs)
def perform_check(txs: pd.DataFrame) -> None:
    assert txs.count(axis=0)["id"] > 2


@node(inputs=txs)
def txs_agg(txs: pd.DataFrame) -> pd.DataFrame:
    return txs.groupby("to").agg({"amount": "sum"})


@node(inputs=txs_agg)
def print_agg(txs_agg: pd.DataFrame) -> None:
    print(txs_agg.to_json())


if __name__ == "__main__":
    print(viz(__name__, fmt="mermaid"))
    run(__name__)
