# Testing nodes

Testing is a fundamental part of any data project.
This guide outlines different strategies for testing nodes and pipelines, which require minimal setup.
As we will see, testing a pipeline is in fact made easier by Ordeq, due to the separation of IO and transformations.

!!! question "New to automated testing?"

    If you are new to automated testing, we recommend starting with exploring [`pytest`][pytest] and a testing guide of the library of your choice.
    For instance, if you use Polars, check out [this guide][polars-testing].

## Testing a single node

Let's start by considering the following basic pipeline node from the [node concepts section][concepts-node].
We have slightly adapted the example to use Polars instead of Spark, since this simplifies the tests.
This pipeline joins transactions and clients data.
The source code of this project can be found [here][testing-nodes-project].

=== "pipeline.py"

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

=== "catalog.py"

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

As we can see in the catalog, the node relies on data that is stored on S3, and a date value that is passed from the command line arguments with which the node is run.
In most cases, this would complicate testing the node, since we have to somehow mimic these dependencies during tests.
With Ordeq, testing is much easier.

Let's create a basic unit test for this node.
We will use [`pytest`][pytest] in this example, but the principles apply to any other testing framework, like `unittest`.
First, we create a `tests` package and a test module with the following content:

=== "tests/test_pipeline.py"

    ```python

    import polars as pl
    from testing_nodes.pipeline import join_txs_and_clients


    def test_join_txs_and_clients():
        # Create the seed data
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

        # Call the method
        actual = join_txs_and_clients(txs, clients, "2023-12-30")

        # Check the output
        expected = pl.DataFrame(
            data=[["2023-12-30", 123, "A", 100, "a very nice client"]],
            schema=["date", "txs_id", "client_id", "amount", "client_name"],
            orient="row",
        )
        assert actual.equals(expected)
    ```

This unit test follows a standard setup: we create some seed data, feed if to the method under test, and compare the output against an expected value.
Unit-testing the node can be done in the same way as unit-testing any Python method, since nodes behave like plain Python functions.

!!! note "Calling the node doesn't load or save any data"
    It is worth nothing that calling the node this does not load or save IOs, and does not invoke hooks.
    This is a good practice for unit tests, as it keeps them fast and isolated.
    We don't need to worry about where the data resides, and can focus on verifying the transformations.

### Running a node in tests

Alternatively, you can test nodes by running them.
This will load the data from the node inputs, and save the returned data to the node outputs.
It will also invoke [hooks][concepts-hooks] that are set on the IO or runner.
Here is how you could run a node as part of a unit test:

=== "tests/test_pipeline.py"

    ```python
    from ordeq import run
    from testing_nodes.pipeline import join_txs_and_clients


    def test_run_node():
        run(join_txs_and_clients)
    ```

In contrast to the tests above, this test _does_ connect to actual data sources, and invokes the hooks.
For instance, running the node will attempt to connect to S3, and parse the date value from a command line argument.
This is not ideal: we would like to test our node with representative data without relying on external resources.

On the other hand, we would still like to test the node in combination with loading or saving IOs.
To achieve this, we can create alternative IOs representing data of the same structure, and use it to test the node.
We can tell the runner to use the alternative IO instead of the actual IO, as shown in the following example:

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

When `join_txs_and_clients` is run, Ordeq will use the test's `txs` and `clients` IOs as replacements for those in the catalog.
This approach works well if you need fine-grained control over which IOs are used during tests.
But it is also quite verbose, and doesn't allow us yet to reuse test data across multiple tests.
The next section introduces a more complete and reusable approach.

!!! info "More on running nodes"

    Running a node from a test works exactly the same as running the node from a production system.
    This improves testability of your project.
    To learn more about how to configure the run of your nodes, for instance how to set alternative hooks during testing, please refer to the [guide][run-and-viz].

### Running with a different catalog

Another way to test your node using alternative data is by running with a dedicated test [catalog][concepts-catalog].
The catalog can be defined in the source folder, as explained in [the guide][concepts-catalog], or in a separate package.
Here is a example of the test package with a test catalog:

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

    ```python hl_lines="6"
    import test_catalog
    import testing_nodes
    import polars as pl

    def test_run_node_catalog():
        run(join_txs_and_clients, io={testing_nodes.catalog: test_catalog})

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
The test catalog is imported in the tests, and passed to the runner.
The runner will use only the entries of the test catalog, without relying on external resources.

!!! tip "Ordeq verifies the test catalog"

    Ordeq verifies that the alternative catalog that is passed to the runner is consistent with the original one.
    This ensures that you accidentally run using a "real" IO during tests.
    More info in the [catalog guide][concepts-catalog].

## Testing more nodes

So far we have covered examples on how to test a single node.
A next step in testing your project would be to test your node in integration with other nodes.
For instance, you might want to run an entire (sub)pipeline and verify the outputs.
To do this, we will again leverage the runner.

We will first adapt the example and include a new node `aggregate_txs` that performs a basic aggregation.
This means our pipeline consists of two nodes in total.
Next, we run this pipeline from the tests, and check the output:

=== "pipeline.py"

    ```python hl_lines="17-21"
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
        run(testing_nodes.pipeline, io={testing_nodes.catalog: test_catalog})

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


!!! question "Questions, suggestions or remarks?"
    If you have any questions, suggestions or remarks on this guide, please feel free to create an [issue on GitHub][issues].

[concepts-catalog]: ../getting-started/concepts/catalogs.md
[concepts-hooks]: ../getting-started/concepts/hooks.md
[concepts-node]: ../getting-started/concepts/nodes.md
[polars-testing]: https://docs.pola.rs/api/python/stable/reference/testing.html
[pytest]: https://docs.pytest.org/en/stable/
[run-and-viz]: ./run_and_viz.md
[run-api]: ../api/ordeq/_runner.md
[testing-nodes-project]: https://github.com/ing-bank/ordeq/tree/main/examples
[issues]: https://github.com/ing-bank/ordeq/issues/new
