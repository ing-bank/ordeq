# Checks

A **check** is a special type of node that is triggered once certain IOs are loaded or saved.
Checks are triggered before other nodes are run.
This can be useful for checking data, like enforcing constraints or running data quality tests.
For example:

- Validating that data conforms to a specific schema (e.g., ensuring correct data types).
- Enforcing business rules on the data (e.g., ensuring that transaction amounts are positive).
- Profiling data to gather statistics or insights (e.g., calculating outliers).

Checks allow you to inject this logic in your pipelines with minimal code changes.

!!! warning "Checks are in preview"

    Checks are currently in preview and may change in future releases without prior notice.

## Defining checks

Here is an example check that validates that a dataset is not empty:

```python hl_lines="8"
import polars as pl
from ordeq import node
from ordeq_polars import PolarsEagerCSV

txs = PolarsEagerCSV(path="s3://my-bucket/txs.csv")


@node(inputs=txs, checks=txs)
def validate_row_count(df: pl.DataFrame) -> None:
    if df.count() == 0:
        raise ValueError("No transactions data found!")
```

Checks are created in the same way as regular nodes, but take a `checks` parameter.
This parameter specifies the IOs that trigger the execution of the check.
For instance:

```python
@node(checks=[a])
def my_check(): ...
```

will run `my_check` after `a` is loaded or saved.

Analogously:

```python
@node(checks=[a, b])
def my_check(): ...
```

will run `my_check` after both `a` and `b` are loaded or saved.

### Checks with inputs

As any node, a check can take inputs.
The inputs can be the same IOs that trigger the check, or different ones.
This allows you to validate the data with additional IOs.
For example, you can perform a check on one IO, using another IO as input:

```python hl_lines="8"
from pathlib import Path

from ordeq_files import JSON

txs_schema = JSON(path=Path("schemas/txs.json"))


@node(inputs=[txs, txs_schema], checks=txs)  # (1)!
def validate_schema(df: pl.DataFrame, schema: dict) -> None:
    if not df.columns == schema["columns"]:
        raise ValueError("Transactions data does not conform to schema!")
```

1. The check is triggered by the `PolarsEagerCSV`, but also takes a `JSON` as input.

This is useful if the check logic requires additional data to perform the validation.
In the example above, this additional data is metadata (the schema), but it could also be other actual data:

```python hl_lines="7"
from ordeq import node
from ordeq_polars import PolarsEagerCSV

txs_countries = PolarsEagerCSV(path="s3://my-bucket/valid-countries.csv")


@node(inputs=[txs, txs_countries], checks=txs)  # (1)!
def validate_txs(df: pl.DataFrame, countries: pl.DataFrame) -> None:
    if df.join(countries, on="country_code", how="anti").count() > 0:
        raise ValueError("Transactions data contains invalid country codes!")
```

1. The check is triggered by the `PolarsEagerCSV`, but also takes another `PolarsEagerCSV` as input.

The check above validates that all country codes in the transactions data are valid by using an additional dataset of valid country codes.

### Checks with outputs

Checks can also produce outputs.
This is useful if you want to store the results of the check for later use, like analysis or reporting.
For example, you can create a check that profiles the data and saves the results to a CSV file:

```python hl_lines="9"
import polars as pl
from ordeq import node
from ordeq_polars import PolarsEagerCSV

txs = PolarsEagerCSV(path="s3://my-bucket/txs.csv")
txs_profile = PolarsEagerCSV(path="s3://my-bucket/txs_profile.csv")


@node(inputs=txs, outputs=txs_profile, checks=txs)  # (1)!
def describe_txs(df: pl.DataFrame) -> pl.DataFrame:
    return df.describe()
```

1. The check is triggered by the `PolarsEagerCSV`, and produces another `PolarsEagerCSV` as output.

It is also possible to reuse an output in other nodes:

```python hl_lines="9 15"
import polars as pl
from ordeq import node
from ordeq_polars import PolarsEagerCSV

txs = PolarsEagerCSV(path="s3://my-bucket/txs.csv")
txs_invalid = PolarsEagerCSV(path="s3://my-bucket/txs-invalid-countries.csv")


@node(inputs=txs, outputs=txs_invalid, checks=txs)  # (1)!
def filter_invalid(df: pl.DataFrame) -> pl.DataFrame:
    valid_codes = ["US", "GB", "DE", "NL"]
    return df.filter(~pl.col("country_code").is_in(valid_codes))


@node(inputs=txs_invalid, checks=txs)  # (2)!
def check_invalid(invalid: pl.DataFrame) -> None:
    if invalid.count() > 0:
        raise ValueError(
            f"Found {invalid.count()} transactions with invalid country codes!"
        )
```

1. The first check filters invalid country codes and produces an output with the invalid rows.
1. The second check uses that output to raise an error if any invalid rows were found.

This is useful since the output of `filter_invalid` can be inspected later, even if `check_invalid` raises an error.
It also means you can build complex validations using checks that depend on other checks.

## Running checks

Checks are automatically run when the IOs that trigger them are loaded or saved.
For example, consider the following pipeline:

=== "pipeline.py"

    ```python
    import catalog
    import polars as pl
    from ordeq import node


    @node(inputs=catalog.txs, outputs=catalog.txs_aggregated)
    def aggregate_txs(txs: pl.DataFrame) -> pl.DataFrame:
        return txs.group_by("client_id").sum()
    ```

=== "checks.py"

    ```python
    import catalog
    import polars as pl
    from ordeq import node


    @node(inputs=catalog.txs, outputs=catalog.txs_invalid, checks=catalog.txs)
    def filter_invalid(df: pl.DataFrame) -> pl.DataFrame:
        valid_codes = ["US", "GB", "DE", "NL"]
        return df.filter(~pl.col("country_code").is_in(valid_codes))


    @node(inputs=catalog.txs_invalid, checks=catalog.txs)
    def check_invalid(invalid: pl.DataFrame) -> None:
        if invalid.count() > 0:
            raise ValueError(
                f"Found {invalid.count()} transactions with invalid country codes!"
            )
    ```

=== "catalog.py"

    ```python
    from ordeq_polars import PolarsEagerCSV

    txs = PolarsEagerCSV(path="s3://my-bucket/txs.csv")
    txs_invalid = PolarsEagerCSV(path="s3://my-bucket/txs-invalid-countries.csv")
    txs_aggregated = PolarsEagerCSV(path="s3://my-bucket/txs-aggregated.csv")
    ```

=== "\_\_main\_\_.py"

    ```python
    import pipeline
    from ordeq import run

    if __name__ == "__main__":
        run(pipeline)
    ```

When the pipeline is run, the following happens:

- `txs` is loaded (as usual)
- `filter_invalid` is run (since it is a check on `txs`)
- `check_invalid` is run (since it is a check on `txs`)
- If `check_invalid` passes without errors, node `aggregate_txs` is run
- `txs_aggregated` is saved (as usual)

That means checks can be added to existing pipelines without modifying existing code.
You only need to define the checks in your project as shown above.
You can run your pipeline as before, and Ordeq will take care of running the checks at the appropriate times.

!!! question "Questions or feedback?"

    If you have any questions or feedback about checks or this guide, please open an issue on [GitHub][issues].

[gx]: https://greatexpectations.io/
[issues]: https://github.com/ing-bank/ordeq/issues/new
[pandera]: https://pandera.readthedocs.io/
