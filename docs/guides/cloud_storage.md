# Cloud storage

Ordeq IO has been designed to work seamlessly with cloud storage services like Amazon S3, Google Cloud Storage and Azure Blob Storage.
Interacting with these services involves certain complexities, like authentication and network communication.
Ordeq IO aims to abstract these complexities from the user, while requiring little code.

## Leveraging client libraries

Many IOs offered by Ordeq leverage client libraries with built-in cloud storage support.
For instance, you can load and save a CSV to S3 using Pandas as follows:

!!! info "Install the `ordeq-pandas` package"

    To follow the example below, you need to install the `ordeq-pandas` package.

```pycon
>>> from ordeq_pandas import PandasCSV
>>> csv = PandasCSV(path="gs://my-bucket/my-data.csv")
>>> csv.load()  # this loads from Google Cloud Storage
   id    name      date   amount
0   1   Alice 2024-01-01     100
1   2     Bob 2024-01-02     150
...
```

Other popular libraries that offer built-in support for cloud storage are DuckDB, Polars and Spark.
Ordeq provides IOs for these libraries in `ordeq-duckdb`, `ordeq-polars` and `ordeq-spark`.
Have a look at the [API reference][api] for more information.

## CloudPath

Another way IOs support cloud storage when built-in support is not present, is by accepting `cloudpathlib`'s `CloudPath`.
CloudPaths abstract away the complexities of interacting with cloud storage like Amazon S3, Google Cloud Storage and Azure Blob Storage.

!!! info "Install `cloudpathlib` to use `CloudPath`"

    To follow the example below, you need to install the `cloudpathlib` package.

The following example loads a JSON from Azure Blob Storage:

```pycon
>>> from cloudpathlib import CloudPath
>>> json = JSON(path=CloudPath("az://my-container/txs.json"))
>>> json.load()  # this loads from Azure Blob Storage
{'transactions': [{'amount': 100, 'date': '2023-01-01'}, ...]}
```

Check out the [cloudpathlib documentation][cloudpathlib] for more information and examples.

Many file-like IOs accept a CloudPath object as path.
Examples include `ordeq_yaml.YAML`, `ordeq_matplotlib.MatplotlibFigure` and `ordeq_altair.AltairChart`.
Check the [API reference][api] for more details.

[api]: ../api/ordeq/types.md
[cloudpathlib]: https://cloudpathlib.drivendata.org/stable/
