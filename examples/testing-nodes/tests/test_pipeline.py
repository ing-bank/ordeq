import polars as pl
from polars.testing import assert_frame_equal
from testing_nodes.pipeline import join_txs_and_clients


def test_join_txs_and_clients():
    txs = pl.DataFrame(
        data=[
            ["2023-12-30", 123, "A", 100],
            ["2023-12-31", 456, "B", 10],
            ["2024-01-01", 789, "A", 80],
            ["2024-02-29", 101, "C", 0],
        ],
        schema=["date", "txs_id", "client_id", "amount"],
        orient="row",
    )
    clients = pl.DataFrame(
        data=[
            ["A", "a very nice client"],
            ["B", "beautiful company"],
            ["C", "company inc."],
        ],
        schema=["client_id", "client_name"],
        orient="row",
    )
    actual = join_txs_and_clients(txs, clients, "2023-12-30")
    expected = pl.DataFrame(
        data=[["2023-12-30", 123, "A", 100, "a very nice client"]],
        schema=["date", "txs_id", "client_id", "amount", "client_name"],
        orient="row",
    )
    assert_frame_equal(actual, expected)


from pathlib import Path

from ordeq import run
from ordeq_common import Literal
from ordeq_polars import PolarsEagerCSV
from testing_nodes import catalog

TEST_RESOURCES_DIR = Path(__file__).resolve().parent.parent / "tests-resources"


def test_run_node():
    # Define alternative IO
    txs = PolarsEagerCSV(path=TEST_RESOURCES_DIR / "txs.csv")
    clients = PolarsEagerCSV(path=TEST_RESOURCES_DIR / "clients.csv")
    txs_and_clients = PolarsEagerCSV(
        path=TEST_RESOURCES_DIR / "txs-and-clients.csv"
    )

    # Run with alternative IO:
    run(
        join_txs_and_clients,
        io={
            catalog.txs: txs,
            catalog.clients: clients,
            catalog.date: Literal("2023-12-30"),
            catalog.txs_and_clients: txs_and_clients,
        },
    )

    # Check the output:
    actual = txs_and_clients.load()
    expected = pl.DataFrame(
        data=[["2023-12-30", 123, "A", 100, "a very nice client"]],
        schema=["date", "txs_id", "client_id", "amount", "client_name"],
        orient="row",
    )
    assert_frame_equal(actual, expected)


import test_catalog
import testing_nodes


def test_run_node_catalog():
    # Run with alternative catalog:
    run(join_txs_and_clients, io={testing_nodes.catalog: test_catalog})

    # Check the output:
    actual = test_catalog.txs_and_clients.load()
    expected = pl.DataFrame(
        data=[["2023-12-30", 123, "A", 100, "a very nice client"]],
        schema=["date", "txs_id", "client_id", "amount", "client_name"],
        orient="row",
    )
    assert_frame_equal(actual, expected)


from testing_nodes import pipeline


def test_pipeline():
    # Run the pipeline with an alternative catalog
    run(pipeline, io={testing_nodes.catalog: test_catalog})

    # Check the output:
    actual = test_catalog.aggregated_txs.load()
    expected = pl.DataFrame(
        data=[["A", "a very nice client", 100]],
        schema=["client_id", "client_name", "amount"],
        orient="row",
    )
    assert_frame_equal(actual, expected)
