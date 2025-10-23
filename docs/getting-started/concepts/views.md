# Views

Views are a special type of node.
They are ideal to reflect common transformations, such as:

- filtering, parsing, casting or selecting data
- converting inputs from one type to another (say, from Pandas to Spark DataFrame)
- selecting a device for model training (say, CPU vs GPU)

Often, we don't want to save the result of these transformations.
Instead, we want to pass along the result directly to a subsequent transformation.
That's exactly what views achieve.

### Example

We will slightly adapt the running example from the [introduction].
Suppose we're tasked to:

- filter a Spark DataFrame `txs` by date
- join the filtered DataFrame with `clients`, and output the result to a Hive table

A first attempt at completing this using Ordeq would look roughly like this:

=== "pipeline.py"

    ```python
    import catalog
    from ordeq import node
    from pyspark.sql import DataFrame


    @node(inputs=[catalog.txs, catalog.date], outputs=[catalog.txs_filtered])
    def filter_by_date(txs: DataFrame, date: str) -> DataFrame:
        return txs.filter(txs.date == date)


    @node(
        inputs=[catalog.txs, catalog.clients, catalog.date],
        outputs=catalog.txs_and_clients,
    )
    def join_txs_and_clients(
        txs: DataFrame, clients: DataFrame, date: str
    ) -> DataFrame:
        return txs.join(clients, on="client_id", how="left")
    ```

=== "catalog.py"

    ```python hl_lines="7"
    from ordeq import IO
    from ordeq_args import CommandLineArg
    from ordeq_spark import SparkHiveTable

    date = CommandLineArg("--date", type=str)
    txs = SparkHiveTable(table="txs")
    txs_filtered = IO()  # Placeholder IO
    clients = SparkHiveTable(table="clients")
    txs_and_clients = SparkHiveTable(table="txs_and_clients")
    ```

=== "\__main__.py"

    ```python
    from nodes import filter_by_date, join_txs_and_clients
    from ordeq import run

    if __name__ == "__main__":
        run(filter_by_date, join_txs_and_clients)
    ```

Here's what we have done:

- to keep the transformations modular, we created two nodes: `filter_by_date` and `join_txs_and_clients`.
- we defined a placeholder IO `txs_filtered` in `catalog.py`.
    This IO is not associated with any actual data source.
    It merely serves to pass the output from one node to the other.

This approach has a couple of downsides:

- the separate placeholder IO seems like overhead
- we have to remember to run both the `filter_by_date` and `join_txs_with_clients`, even though `filter_by_date` will never be run individually
- it's not obvious how to reuse `filter_by_date` with different IO, while it does seem a very common transformation

### Using views

Using views, we can edit the example above to as follows:

=== "pipeline.py"

    ```python
    import catalog
    from ordeq import node
    from pyspark.sql import DataFrame


    @node(inputs=[catalog.txs, catalog.date])
    def txs_filtered(txs: DataFrame, date: str) -> DataFrame:
        return txs.filter(txs.date == date)


    @node(inputs=[txs_filtered, catalog.clients], outputs=catalog.txs_and_clients)
    def join_txs_and_clients(
        txs: DataFrame, clients: DataFrame, date: str
    ) -> DataFrame:
        return txs.join(clients, on="client_id", how="left")
    ```

=== "catalog.py"

    ```python hl_lines="7"
    from ordeq import IO
    from ordeq_args import CommandLineArg
    from ordeq_spark import SparkHiveTable

    date = CommandLineArg("--date", type=str)
    txs = SparkHiveTable(table="txs")
    clients = SparkHiveTable(table="clients")
    txs_and_clients = SparkHiveTable(table="txs_and_clients")
    ```

=== "\_\_main\_\_.py"

    ```python
    from nodes import join_txs_and_clients
    from ordeq import run

    if __name__ == "__main__":
        run(join_txs_and_clients)
    ```

Let's break this down:

- we have defined a view `txs_filtered`. Views have no outputs, but may take inputs. In this case, the inputs are the same as those of the previous `filter_by_date` node.
- we pass the view `txs_filtered` directly as input to the node `join_txs_with_clients`

By setting the view as input to the node, Ordeq will pass along the result of `txs_filtered` to `join_txs_with_clients`, without the need for a placeholder IO.
In addition, it will automatically run `txs_filtered` once `join_txs_with_clients` is run.
This greatly simplifies the run command.
