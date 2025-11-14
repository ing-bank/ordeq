# Introduction

We have all been there. As your data project grows:

- Logic gets tightly coupled
- Repetitive tasks are duplicated
- Complexity increases

Ordeq tackles these problems by providing a simple yet powerful way to define IO and transformations throughout your
project.

## How Ordeq helps

Let's see how Ordeq helps you develop data pipelines.
We will start with a simple example.
Here is how a simple data pipeline looks like without Ordeq:

```python title="__main__.py"
from pyspark.sql import SparkSession

if __name__ == "__main__":
    spark = SparkSession.builder.getOrCreate()
    txs = spark.table("txs")
    clients = spark.table("clients")
    txs_and_clients = txs.join(clients, on="client_id", how="left")
    txs_and_clients.write.mode("overwrite").saveAsTable("txs_and_clients")
```

!!! example "Ordeq works with any data processing tool"

    The example above uses PySpark, since it is a popular data processing tool, but the same principles apply to other tools.
    If you are not familiar with Spark, imagine the same logic implemented with Pandas, Dask, or another tool of your choice.

Suppose we want to add a bit more logic, such as filtering the data by a certain date:

```python hl_lines="6 7 8 10" title="__main__.py"
from pyspark.sql import SparkSession
from argparse import ArgumentParser

if __name__ == "__main__":
    spark = SparkSession.builder.getOrCreate()
    parser = ArgumentParser()
    parser.add_argument("--date", type=str)
    date = parser.parse_args().date
    txs = spark.table("txs")
    txs = txs.filter(txs.date == date)
    clients = spark.table("clients")
    txs_and_clients = txs.join(clients, on="client_id", how="left")
    txs_and_clients.write.mode("overwrite").saveAsTable("txs_and_clients")
```

The code is getting more complex, and now you have to pass the date argument every time you run the script.
Also, the logic is still tightly coupled, and you cannot easily reuse parts of it.

### Improvements

Can we do better?
Let's try to modularize the logic by splitting it into functions:

```python hl_lines="5 6 9 10 13-16 19-21" title="__main__.py"
from pyspark.sql import DataFrame, SparkSession
from argparse import ArgumentParser


def load_table(spark: SparkSession, table: str) -> DataFrame:
    return spark.table(table)


def save_table(df: DataFrame, table: str):
    df.write.mode("overwrite").saveAsTable(table)


def parse_date() -> str:
    parser = ArgumentParser()
    parser.add_argument("--date", type=str)
    return parser.parse_args().date


def join_txs_and_clients(txs: DataFrame, clients: DataFrame, date: str):
    txs = txs.filter(txs.date == date)
    return txs.join(clients, on="client_id", how="left")


if __name__ == "__main__":
    spark = SparkSession.builder.getOrCreate()
    date = parse_date()
    txs = load_table(spark, "txs")
    clients = load_table(spark, "clients")
    txs_and_clients = join_txs_and_clients(txs, clients, date)
    save_table(txs_and_clients, "txs_and_clients")
```

This is much better! Each piece of logic can be tested in isolation.
You can reuse the functions in other parts of your project.
However, there are still some challenges.
You still need to route `spark`, `date`, `txs` and `clients` through the functions.
This _couples_ the IO with the transformations.

### The Ordeq solution

Ordeq dissolves the coupling by separating IO, like Spark tables and command line argument, from the transformations.
While the transformations reside in `pipeline.py`, IOs are defined in a separate `catalog` module.
Lastly, a `__main__.py` module takes care of running the job:

=== "pipeline.py"

    ```python
    import catalog
    from ordeq import node
    from pyspark.sql import DataFrame


    @node(
        inputs=[catalog.txs, catalog.clients, catalog.date],
        outputs=catalog.txs_and_clients,
    )
    def join_txs_and_clients(
        txs: DataFrame, clients: DataFrame, date: str
    ) -> DataFrame:
        txs = txs.filter(txs.date == date)
        return txs.join(clients, on="client_id", how="left")
    ```

=== "catalog.py"

    ```python
    from ordeq_args import CommandLineArg
    from ordeq_spark import SparkHiveTable

    # Input IOs
    date = CommandLineArg("--date", type=str)
    txs = SparkHiveTable(table="txs")
    clients = SparkHiveTable(table="clients")

    # Output IOs
    txs_and_clients = SparkHiveTable(table="txs_and_clients")
    ```

=== "\__main__.py"

    ```python
    import logging

    from ordeq import run
    from pipeline import join_txs_and_clients

    # Enable logging
    logging.basicConfig(level=logging.INFO)

    if __name__ == "__main__":
        run(join_txs_and_clients)
    ```

=== "Pipeline Diagram"

    ```mermaid
    graph TB
        subgraph legend["Legend"]
    	direction TB
    	subgraph Objects
    		L0(["Node"]):::node
    		L1[("IO")]:::io
    	end
    	subgraph IO Types
    		L00[("CommandLineArg")]:::io0
    		L01[("SparkHiveTable")]:::io1
    	end
    end

    IO0 --> join_txs_and_clients
    IO1 --> join_txs_and_clients
    IO2 --> join_txs_and_clients
    join_txs_and_clients --> IO3

    subgraph pipeline["Pipeline"]
    	direction TB
    	join_txs_and_clients(["join_txs_and_clients"]):::node
    	IO0[("txs")]:::io1
    	IO1[("clients")]:::io1
    	IO2[("date")]:::io0
    	IO3[("txs_and_clients")]:::io1
    end

    classDef node fill:#008AD7,color:#FFF
    classDef io fill:#FFD43B
    classDef io0 fill:#66c2a5
    classDef io1 fill:#fc8d62

    ```

    !!! tip "Visualising pipelines with Ordeq"

        This diagram is auto-generated by Ordeq. See [Run and Viz](../guides/run_and_viz.md) for more information.

The idea behind the separation is that changes to the IO should not affect the transformations, and vice versa.
Furthermore, the separation helps you keep your project organized.

### Decoupling in practice

#### Changing IO

Say you want to read the transactions from a Iceberg table instead of a Hive table,
you only need to change `catalog.py`.

=== "pipeline.py"

    ```python
    import catalog
    from ordeq import node
    from pyspark.sql import DataFrame


    @node(
        inputs=[catalog.txs, catalog.clients, catalog.date],
        outputs=catalog.txs_and_clients,
    )
    def join_txs_and_clients(
        txs: DataFrame, clients: DataFrame, date: str
    ) -> DataFrame:
        txs = txs.filter(txs.date == date)
        return txs.join(clients, on="client_id", how="left")
    ```

=== "catalog.py"

    ```python hl_lines="6"
    from ordeq_args import CommandLineArg
    from ordeq_spark import SparkHiveTable

    # Input IOs
    date = CommandLineArg("--date", type=str)
    txs = SparkIcebergTable(table="txs")
    clients = SparkHiveTable(table="clients")

    # Output IOs
    txs_and_clients = SparkHiveTable(table="txs_and_clients")
    ```

=== "\__main__.py"

    ```python
    import logging

    from ordeq import run
    from pipeline import join_txs_and_clients

    # Enable logging
    logging.basicConfig(level=logging.INFO)

    if __name__ == "__main__":
        run(join_txs_and_clients)
    ```

=== "Pipeline Diagram"

    ```mermaid
    graph TB
    subgraph legend["Legend"]
    	direction TB
    	subgraph Objects
    		L0(["Node"]):::node
    		L1[("IO")]:::io
    	end
    	subgraph IO Types
    		L00[("CommandLineArg")]:::io0
    		L01[("SparkHiveTable")]:::io1
    		L02[("SparkIcebergTable")]:::io2
    	end
    end

    IO0 --> join_txs_and_clients
    IO1 --> join_txs_and_clients
    IO2 --> join_txs_and_clients
    join_txs_and_clients --> IO3

    subgraph pipeline["Pipeline"]
    	direction TB
    	join_txs_and_clients(["join_txs_and_clients"]):::node
    	IO0[("txs")]:::io2
    	IO1[("clients")]:::io1
    	IO2[("date")]:::io0
    	IO3[("txs_and_clients")]:::io1
    end

    classDef node fill:#008AD7,color:#FFF
    classDef io fill:#FFD43B
    classDef io0 fill:#66c2a5
    classDef io1 fill:#fc8d62
    classDef io2 fill:#8da0cb

    ```

Or, maybe the date comes from an environment variable instead of a command line argument:

=== "pipeline.py"

    ```python
    import catalog
    from ordeq import node
    from pyspark.sql import DataFrame


    @node(
        inputs=[catalog.txs, catalog.clients, catalog.date],
        outputs=catalog.txs_and_clients,
    )
    def join_txs_and_clients(
        txs: DataFrame, clients: DataFrame, date: str
    ) -> DataFrame:
        txs = txs.filter(txs.date == date)
        return txs.join(clients, on="client_id", how="left")
    ```

=== "catalog.py"

    ```python hl_lines="1 5"
    from ordeq_args import EnvironmentVariable
    from ordeq_spark import SparkIcebergTable, SparkHiveTable

    # Input IOs
    date = EnvironmentVariable("DATE")
    txs = SparkIcebergTable(table="txs")
    clients = SparkHiveTable(table="clients")

    # Output IOs
    txs_and_clients = SparkHiveTable(table="txs_and_clients")
    ```

=== "\__main__.py"

    ```python
    import logging

    from ordeq import run
    from pipeline import join_txs_and_clients

    # Enable logging
    logging.basicConfig(level=logging.INFO)

    if __name__ == "__main__":
        run(join_txs_and_clients)
    ```

=== "Pipeline Diagram"

    ```mermaid
    graph TB
    subgraph legend["Legend"]
    	direction TB
    	subgraph Objects
    		L0(["Node"]):::node
    		L1[("IO")]:::io
    	end
    	subgraph IO Types
    		L00[("EnvironmentVariable")]:::io0
    		L01[("SparkHiveTable")]:::io1
    		L02[("SparkIcebergTable")]:::io2
    	end
    end

    IO0 --> join_txs_and_clients
    IO1 --> join_txs_and_clients
    IO2 --> join_txs_and_clients
    join_txs_and_clients --> IO3

    subgraph pipeline["Pipeline"]
    	direction TB
    	join_txs_and_clients(["join_txs_and_clients"]):::node
    	IO0[("txs")]:::io2
    	IO1[("clients")]:::io1
    	IO2[("date")]:::io0
    	IO3[("txs_and_clients")]:::io1
    end

    classDef node fill:#008AD7,color:#FFF
    classDef io fill:#FFD43B
    classDef io0 fill:#66c2a5
    classDef io1 fill:#fc8d62
    classDef io2 fill:#8da0cb


    ```

Perhaps you want to append data to the `txs_and_clients` table instead of overwriting it:

=== "pipeline.py"

    ```python
    import catalog
    from ordeq import node
    from pyspark.sql import DataFrame


    @node(
        inputs=[catalog.txs, catalog.clients, catalog.date],
        outputs=catalog.txs_and_clients,
    )
    def join_txs_and_clients(
        txs: DataFrame, clients: DataFrame, date: str
    ) -> DataFrame:
        txs = txs.filter(txs.date == date)
        return txs.join(clients, on="client_id", how="left")
    ```

=== "catalog.py"

    ```python hl_lines="10-13"
    from ordeq_args import EnvironmentVariable
    from ordeq_spark import SparkIcebergTable, SparkHiveTable

    # Input IOs
    date = EnvironmentVariable("DATE")
    txs = SparkIcebergTable(table="txs")
    clients = SparkHiveTable(table="clients")

    # Output IOs
    txs_and_clients = SparkHiveTable(table="txs_and_clients").with_save_options(
        mode="append"
    )
    ```

=== "\__main__.py"

    ```python
    import logging

    from ordeq import run
    from pipeline import join_txs_and_clients

    # Enable logging
    logging.basicConfig(level=logging.INFO)

    if __name__ == "__main__":
        run(join_txs_and_clients)
    ```

=== "Pipeline Diagram"

    ```mermaid
    graph TB
    subgraph legend["Legend"]
    	direction TB
    	subgraph Objects
    		L0(["Node"]):::node
    		L1[("IO")]:::io
    	end
    	subgraph IO Types
    		L00[("EnvironmentVariable")]:::io0
    		L01[("SparkHiveTable")]:::io1
    		L02[("SparkIcebergTable")]:::io2
    	end
    end

    IO0 --> join_txs_and_clients
    IO1 --> join_txs_and_clients
    IO2 --> join_txs_and_clients
    join_txs_and_clients --> IO3

    subgraph pipeline["Pipeline"]
    	direction TB
    	join_txs_and_clients(["join_txs_and_clients"]):::node
    	IO0[("txs")]:::io2
    	IO1[("clients")]:::io1
    	IO2[("date")]:::io0
    	IO3[("txs_and_clients")]:::io1
    end

    classDef node fill:#008AD7,color:#FFF
    classDef io fill:#FFD43B
    classDef io0 fill:#66c2a5
    classDef io1 fill:#fc8d62
    classDef io2 fill:#8da0cb

    ```

All changes above require only amendments to `catalog.py`.
The transformations in `pipeline.py` remain unchanged.
Furthermore, each IO is defined once and can be reused throughout your project.

#### Changing transformations

Vice versa, if you want to change the logic of how transactions and clients are joined, you only need to change `pipeline.py`.
For example, you might want to filter out inactive clients and transactions with a non-positive amount:

=== "pipeline.py"

    ```python hl_lines="14-17"
    from ordeq import node
    import catalog


    @node(
        inputs=[catalog.txs, catalog.clients, catalog.date],
        outputs=catalog.txs_and_clients,
    )
    def join_txs_and_clients(
        txs: DataFrame, clients: DataFrame, date: str
    ) -> DataFrame:
        txs = txs.filter(txs.date == date)
        txs_and_clients = txs.join(clients, on="client_id", how="inner")
        return txs_and_clients.where(
            (txs_and_clients.amount > 0) & (txs_and_clients.status == "active")
        )
    ```

=== "catalog.py"

    ```python
    from ordeq_args import EnvironmentVariable
    from ordeq_spark import SparkHiveTable, SparkIcebergTable

    # Input IOs
    date = EnvironmentVariable("DATE")
    txs = SparkIcebergTable(table="txs")
    clients = SparkHiveTable(table="clients")

    # Output IOs
    txs_and_clients = SparkHiveTable(table="txs_and_clients").with_save_options(
        mode="append"
    )
    ```

=== "\__main__.py"

    ```python
    import logging

    from ordeq import run
    from pipeline import join_txs_and_clients

    # Enable logging
    logging.basicConfig(level=logging.INFO)

    if __name__ == "__main__":
        run(join_txs_and_clients)
    ```

=== "Pipeline Diagram"

    ```mermaid
    graph TB
    subgraph legend["Legend"]
    	direction TB
    	subgraph Objects
    		L0(["Node"]):::node
    		L1[("IO")]:::io
    	end
    	subgraph IO Types
    		L00[("EnvironmentVariable")]:::io0
    		L01[("SparkHiveTable")]:::io1
    		L02[("SparkIcebergTable")]:::io2
    	end
    end

    IO0 --> join_txs_and_clients
    IO1 --> join_txs_and_clients
    IO2 --> join_txs_and_clients
    join_txs_and_clients --> IO3

    subgraph pipeline["Pipeline"]
    	direction TB
    	join_txs_and_clients(["join_txs_and_clients"]):::node
    	IO0[("txs")]:::io2
    	IO1[("clients")]:::io1
    	IO2[("date")]:::io0
    	IO3[("txs_and_clients")]:::io1
    end

    classDef node fill:#008AD7,color:#FFF
    classDef io fill:#FFD43B
    classDef io0 fill:#66c2a5
    classDef io1 fill:#fc8d62
    classDef io2 fill:#8da0cb

    ```

The example above only changes the `join_txs_and_clients` node.
What if we want to add more nodes?
For example, we might want to add a node that aggregates the transaction amount by client:

=== "pipeline.py"

    ```python hl_lines="19-26"
    from ordeq import node
    import catalog


    @node(
        inputs=[catalog.txs, catalog.clients, catalog.date],
        outputs=catalog.txs_and_clients,
    )
    def join_txs_and_clients(
        txs: DataFrame, clients: DataFrame, date: str
    ) -> DataFrame:
        txs = txs.filter(txs.date == date)
        txs_and_clients = txs.join(clients, on="client_id", how="inner")
        return txs_and_clients.where(
            (txs_and_clients.amount > 0) & (txs_and_clients.status == "active")
        )


    @node(inputs=catalog.txs_and_clients, outputs=catalog.aggregated_txs)
    def aggregate_txs(txs_and_clients: DataFrame) -> DataFrame:
        return txs_and_clients.groupBy("client_id").sum("amount")
    ```

=== "catalog.py"

    ```python hl_lines="15-17"
    from ordeq_args import EnvironmentVariable
    from ordeq_spark import SparkIcebergTable, SparkHiveTable

    # Input IOs
    date = EnvironmentVariable("DATE")
    txs = SparkIcebergTable(table="txs")
    clients = SparkHiveTable(table="clients")

    # Intermediate IOs
    txs_and_clients = SparkHiveTable(table="txs_and_clients").with_save_options(
        mode="append"
    )

    # Output IOs
    aggregated_txs = SparkHiveTable(table="aggregated_txs").with_save_options(
        partition_by="date"
    )
    ```

=== "\__main__.py"

    ```python hl_lines="4 10-13"
    import logging

    from ordeq import run
    import pipeline

    # Enable logging
    logging.basicConfig(level=logging.INFO)

    if __name__ == "__main__":
        run(pipeline)
        # This is equivalent to running:
        # from pipeline import join_txs_and_clients, aggregate_txs
        # >>> run(join_txs_and_clients, aggregate_txs)
    ```

=== "Pipeline Diagram"

    ```mermaid
    graph TB
    subgraph legend["Legend"]
    	direction TB
    	subgraph Objects
    		L0(["Node"]):::node
    		L1[("IO")]:::io
    	end
    	subgraph IO Types
    		L00[("EnvironmentVariable")]:::io0
    		L01[("SparkHiveTable")]:::io1
    		L02[("SparkIcebergTable")]:::io2
    	end
    end

    IO0 --> join_txs_and_clients
    IO1 --> join_txs_and_clients
    IO2 --> join_txs_and_clients
    join_txs_and_clients --> IO3
    IO3 --> aggregate_txs
    aggregate_txs --> IO4

    subgraph pipeline["Pipeline"]
    	direction TB
    	join_txs_and_clients(["join_txs_and_clients"]):::node
    	aggregate_txs(["aggregate_txs"]):::node
    	IO0[("txs")]:::io2
    	IO1[("clients")]:::io1
    	IO2[("date")]:::io0
    	IO3[("txs_and_clients")]:::io1
    	IO4[("aggregated_txs")]:::io1
    end

    classDef node fill:#008AD7,color:#FFF
    classDef io fill:#FFD43B
    classDef io0 fill:#66c2a5
    classDef io1 fill:#fc8d62
    classDef io2 fill:#8da0cb

    ```

This example shows how easy it is to grow and maintain your project with Ordeq.
You can add new nodes and IO without changing existing code.
Each transformation is modular and isolated.

#### Running the pipeline

Meanwhile, the `run` function takes care of loading the inputs and saving the outputs of each node.
You no longer need to route the inputs and outputs of each transformation through the functions.
Dependencies between nodes are automatically resolved.

!!! success "Where to go from here?"

    - Learn more about Ordeqs [core concepts](./concepts/io.md)
