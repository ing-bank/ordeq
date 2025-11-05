from pathlib import Path

from ordeq_common import Literal
from ordeq_polars import PolarsEagerCSV

# Directory for test data:
TEST_RESOURCES_DIR = Path(__file__).resolve().parent.parent / "tests-resources"

date = Literal("2023-12-30")
txs = PolarsEagerCSV(path=TEST_RESOURCES_DIR / "txs.csv")
clients = PolarsEagerCSV(path=TEST_RESOURCES_DIR / "clients.csv")
txs_and_clients = PolarsEagerCSV(
    path=TEST_RESOURCES_DIR / "txs-and-clients.csv"
)
aggregated_txs = PolarsEagerCSV(path=TEST_RESOURCES_DIR / "aggregated-txs.csv")
