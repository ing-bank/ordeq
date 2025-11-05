# Testing nodes

This guide outlines different strategies for testing nodes and pipelines.
Testing an Ordeq project is easy and requires minimal setup.
Because nodes behave like plain Python functions, they can be tested using any Python testing framework.

## Testing a single node

Let's start by considering the following basic pipeline node from the [node concepts section][concepts-node].
We have slightly adapted the pipeline to use Polars instead of Spark.
This pipeline joins transactions data with clients data.
The source code of this project can be found [here][testing-nodes-project].

=== "src/testing_nodes/pipeline.py"

    ```python
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
        txs = txs.filter(txs["date"] == date)
        return txs.join(clients, on="client_id", how="left")
    ```

=== "src/starter_testing/catalog.py"

    ```python
    from ordeq_args import CommandLineArg
    from ordeq_polars import PolarsEagerParquet

    date = CommandLineArg("--date", type=str)
    txs = PolarsEagerParquet(path="s3://bucket/txs.parquet")
    clients = PolarsEagerParquet(path="s3://bucket/clients.parquet")
    txs_and_clients = PolarsEagerParquet(
        path="s3://bucket/txs_and_clients.parquet"
    )
    ```

As we can see in the catalog, this node depends on data on S3, and a date value that is passed as command line argument.
In most cases, this would complicate unit testing, but with Ordeq it doesn't!
Let's start by creating some unit tests for this node.
We will use [`pytest`][pytest] to test our project, but the principles also apply to other testing framework like
`unittest`.
First, we will create a `tests` package and a test module `test_pipeline.py`.
This module contains a basic unit tests for the node:

=== "tests/test_pipeline.py"

    ```python

    import polars as pl
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
        assert actual.equals(expected)
    ```

Unit-testing the node like can be done in the same way as unit-testing any Python method.
Calling the node doesn't incur any overhead compared to a regular method.
It does not load or save IOs, and does not call hooks.
This is a good practice for unit tests, as it keeps them fast and isolated.

### Running a node in tests

Alternatively, you can test nodes by running them.
This will load the data from the node inputs, and save the returned data to the node outputs.
It will also invoke [hooks][concepts-hooks] that are set on the IO or runner.

=== "tests/test_pipeline.py"

    ```python
    from ordeq import run
    from testing_nodes.pipeline import join_txs_and_clients


    def test_run_node():
        # Run with alternative IO:
        run(join_txs_and_clients)
        # do your assertions ...
    ```

In contrast to the tests above, this test does depend on the content of the data.

### Running with different IO

Many times we do not want to connect to a real file system or database when testing.
This can be because connecting to the real data is slow, or because we do not want the tests to change the actual data.
Instead, we want to test the logic with some seed data, often stored locally.

For example, suppose reading from `txs` is very expensive, because it is a large file.
We can then use a local file, with the same structure, to test the node.
To run the node with different IO, simply set the `io` argument of the runner:

=== "tests/test_pipeline.py"

    ```python
    from pathlib import Path

    import polars as pl
    from ordeq import run
    from ordeq_common import Literal
    from ordeq_polars import PolarsEagerCSV
    from testing_nodes import catalog
    from testing_nodes.pipeline import join_txs_and_clients

    # Directory with test data:
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
        assert actual.equals(expected)
    ```

When `join_txs_and_clients` is run, Ordeq will use the test's `txs` and `clients` IOs as replacements of those in the catalog.

!!! info "More on running nodes"

    Running a node from a test works exactly the same as running the node from a production system.
    This improves testability of your project.
    To learn more about how to configure the run of your nodes, for instance how to set alternative hooks during testing, please refer to the [guide][run-and-viz].

### Running with a different catalog

Another way to test your node using alternative data is by running it with a dedicated test [catalog][concepts-catalog].
The catalog can be defined in the source folder, as explained in [the guide][concepts-catalog], or in a separate package.
Here is a simple overview of your test package with a test catalog:

=== "tests/test_catalog.py"

    ```python
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
    ```

=== "tests/test_pipeline.py"

    ```python
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
        assert actual.equals(expected)
    ```

The test catalog defines the same entries as the source catalog, but points to different data.
In this case, the test data is stored in a `tests-resources` folder, but you can store it anywhere.
The test catalog module is imported in the tests, and passed to the runner.
Because `testing_nodes.catalog` is mapped to `test_catalog`, Ordeq will replace all entries of the source catalog with those of test catalog.

## Testing more nodes

So far we have covered examples on how to test a single node.
A next step in testing your project would be to test your node in integration with other nodes.
For instance, you might want to run an entire (sub)pipeline and verify the outputs.
To do this, we will again leverage the runner.

=== "pipeline.py" hl_lines=1-3

    ```python
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
        txs = txs.filter(txs["date"] == date)
        return txs.join(clients, on="client_id", how="left")


    @node(inputs=catalog.txs_and_clients, outputs=catalog.aggregated_txs)
    def aggregate_txs(txs_and_clients: pl.DataFrame) -> pl.DataFrame:
        return txs_and_clients.group_by("client_id", "client_name").agg(
            pl.sum("amount")
        )
    ```

=== "tests/test_pipeline.py"

    ```python
    import polars as pl
    import test_catalog
    import testing_nodes


    def test_pipeline():
        # Run the entire pipeline with an alternative catalog
        run(testing_nodes.pipeline, io={testing_nodes.catalog: test_catalog})

        # Check the output:
        actual = test_catalog.aggregated_txs.load()
        expected = pl.DataFrame(
            data=[["A", "a very nice client", 100]],
            schema=["client_id", "client_name", "amount"],
            orient="row",
        )
        assert actual.equals(expected)
    ```

Because `run` runs the (sub)pipeline under test in exactly the same way as it would in a production setting, you can test the actual pipeline behaviour.
For more information on how to set up the run, please see the [guide][run-and-viz] or check out the [API reference][run-api].

[concepts-catalog]: ../getting-started/concepts/catalogs.md
[concepts-hooks]: ../getting-started/concepts/hooks.md
[concepts-node]: ../getting-started/concepts/nodes.md
[pytest]: https://docs.pytest.org/en/stable/
[run-and-viz]: ./run_and_viz.md
[run-api]: ../api/ordeq/_runner.md
