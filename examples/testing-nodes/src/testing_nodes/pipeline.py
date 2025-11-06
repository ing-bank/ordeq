import polars as pl
from ordeq import node

from testing_nodes import catalog


@node(
    inputs=[catalog.txs, catalog.clients, catalog.date],
    outputs=catalog.txs_and_clients,
)
def join_txs_and_clients(
    txs: pl.DataFrame, clients: pl.DataFrame, date
) -> pl.DataFrame:
    """Joins transactions with client data.

    Args:
        txs: Transactions data.
        clients: Clients data.
        date: Date to process.

    Returns:
        The joined data.
    """
    txs = txs.filter(txs["date"] == date)
    return txs.join(clients, on="client_id", how="left")


@node(inputs=catalog.txs_and_clients, outputs=catalog.aggregated_txs)
def aggregate_txs(txs_and_clients: pl.DataFrame) -> pl.DataFrame:
    """Aggregates transaction amount by client

    Args:
        txs_and_clients: The transactions and client info.

    Returns:
        The aggregated amount.
    """
    return txs_and_clients.group_by("client_id", "client_name").agg(
        pl.sum("amount")
    )
