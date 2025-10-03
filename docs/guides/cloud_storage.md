# Cloud storage

Ordeq IO has been designed to work seamlessly with cloud storage services like Amazon S3, Google Cloud Storage and Azure
Blob Storage.
Interacting with these services involves certain complexities, like authentication and network communication.
Ordeq IO abstracts these complexities from the user.

We will discuss three ways to operate on cloud storage:

- Leveraging built-in support
- Using IO with CloudPath
- Low-level IO

## Leveraging built-in support

Many IOs offered by Ordeq provide built-in support for cloud storage.
For instance, you can load and save a CSV to S3 using the `ordeq_pandas.PandasCSV` as follows:

```pycon
>>> from ordeq_pandas import PandasCSV
>>> csv = PandasCSV(path="gs://my-bucket/my-data.csv")
>>> csv.load()  # this loads from Google Cloud Storage
   id    name      date   amount
0   1   Alice 2024-01-01     100
1   2     Bob 2024-01-02     150
```

Whether the IO offers built-in support for cloud storage is often dependent on the client library that it delegates to.
For instance, `PandasCSV` uses `pd.read_csv` and `DataFrame.to_csv` under the hood.
Other IOs that offer built-in support for cloud storage are offered in `ordeq-duckdb`, `ordeq-spark` and `ordeq-polars`.
Have a look at the [API reference][api] for more information.

The built-in approach is straightforward and works well for many use cases.
The client library often handles the interaction with cloud storage efficiently.
For instance, if the client library is written in C, it can be faster than a pure Python implementation.

This approach does not work well if the client library does not expose all options that you need.
You may require more complex authentication schemes.
Have a look at the documentation of the client library to see what options are available.

## Using IO with CloudPath

Another way to work with cloud storage is to use `cloudpathlib`'s `CloudPath`.
This abstracts away the complexities of interacting with cloud storage.
The following example loads a JSON from a local path:

```pycon
>>> from ordeq_json import JSON
>>> from pathlib import Path
>>> local_json = JSON(path=Path("txs.json"))
>>> local_json.load() # this loads from local
{'transactions': [{'amount': 10, 'date': '2024-12-28'}, ...]}
```

!!! note "Install `cloudpathlib` to use `CloudPath`"

    To follow the example below, you need to install the `cloudpathlib` package.

CloudPath allows you to exchange the local path with a path on Amazon S3, Azure Blob Storage and Google Cloud Storage:

```pycon
>>> from cloudpathlib import CloudPath
>>> json = JSON(path=CloudPath("az://my-container/txs.json"))
>>> json.load()  # this loads from Azure Blob Storage
{'transactions': [{'amount': 100, 'date': '2023-01-01'}, ...]}
```

Check out the [cloudpathlib documentation][cloudpathlib] for more information and examples.

Many file-like IOs accept a `CloudPath` object as path.
Examples include `ordeq_files.YAML`, `ordeq_matplotlib.MatplotlibFigure` and `ordeq_altair.AltairChart`.
Check the [API reference][api] for more details.

Using a CloudPath is great option if the client library used by the IO does not (fully) support cloud storage.
A possible limitation is that CloudPath may not support all low-level features of the underlying cloud storage service.

## Using a low-level IO

The third option is to use a low-level IO.
This provides more control over the interaction with cloud storage.
An example of such a low-level IO is `S3Object` from the `ordeq_boto3` package.
This IO interacts with Amazon S3 using the `boto3` client library.

Here is an example of an `S3Object` that loads a JSON file from S3:

```pycon
>>> from ordeq_boto3 import S3Object
>>> obj = S3Object(bucket_name="my-bucket", object_key="my-data.json")
>>> obj.load()
b'{'transactions': [{'amount': 100, 'date': '2023-01-01'
```

This approach gives you more control over the interaction with the cloud storage service.
For instance, you can specify options specific to S3:

```pycon
>>> from datetime import datetime
>>> obj.load(IfModifiedSince=datetime(2015, 1, 1))
b'{'transactions': [{'amount': 100, 'date': '2023-01-01'
>>> obj.save(ACL="authenticated-read")
```

The low-level IO is a light-weight choice, as it avoids the overhead of a higher-level abstraction.
It's also ideal if you want to access the raw object data, rather than a converted representation.
However, it also requires more knowledge about the API of the library used by the low-level IO.

## Conclusion

In this guide, we explored three ways to work with cloud storage data using Ordeq IOs.
When choosing your approach, you can consider the following best practices:

- Check whether Ordeq offers IOs for the client library of your choice.
    If not, you can [create a custom IO][custom-io] or [contribute] to Ordeq by adding the IO.
- If the IO does not offer built-in support for cloud storage, check if it accepts a CloudPath.
    This works best for file-like IOs like YAML, JSON or Parquet files.
- If you need more control on the interaction, or you prefer working with raw data, use a low-level IO like `ordeq_boto3.S3Object`.

[api]: ../api/ordeq/types.md
[cloudpathlib]: https://cloudpathlib.drivendata.org/stable/
[contribute]: ../CONTRIBUTING.md
[custom-io]: ./custom_io.md
