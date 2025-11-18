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
        "country": ["NL", "BE", "US"],
    })
)
txs_agg_invalid = IO[Any]()


@node(inputs=txs)
def txs_agg(txs: pd.DataFrame) -> pd.DataFrame:
    return txs.groupby("country").agg({"amount": "sum"})


@node(inputs=txs_agg, checks=txs_agg)
def perform_check(txs_agg: pd.DataFrame) -> None:
    countries = set(txs_agg.index.values) - {"NL", "BE"}
    assert len(countries) == 0, "Invalid countries found: " + ", ".join(
        countries
    )


@node(inputs=txs_agg)
def print_agg(txs_agg: pd.DataFrame) -> None:
    print(txs_agg.to_json())


if __name__ == "__main__":
    print(viz(__name__, fmt="mermaid"))
    run(__name__)
