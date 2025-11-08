from typing import TypeVar, Any

from ordeq._io import AnyIO

Tio = TypeVar("Tio", bound=AnyIO)


def _has_resources(io: AnyIO) -> bool:
    return hasattr(io, "__resources__")


def _has_references(io: AnyIO) -> bool:
    return hasattr(io, "references")


class Resource:
    """A resource represents a physical data object, like a file or a table.
    Resources are used to identify the underlying data that is being loaded or
    saved by IOs. This is necessary because the same resource can be loaded or
    saved in multiple ways, depending on the IO implementation.

    For instance: both `ordeq_pandas.PandasCSV` and `ordeq_files.CSV` read a
    CSV file, but `PandasCSV` loads it as a DataFrame, while `CSV` loads
    raw rows.

    Two IOs that process the same resource can exist in the same project for a
    variety of reasons. For instance, suppose you want to first copy a raw file
    from one location to another, and then manipulate it using Pandas.

    Shared resources should be identified to determine the topological sorting
    of nodes. In the example above: the node processing the raw file
    should be scheduled before the node that manipulates the data with Pandas.

    The resource used by an IO can often be derived from the IO attributes. For
    instance, most file-like IOs have a `path` attribute pointing to the file
    address. But IO attributes are typically tied to the library that performs
    the actual IO, and different libraries make different choices as to
    what (type of) attributes they expect and accept.

    For instance: the `path` attribute of `PandasCSV` accepts a URI of files
    on cloud storage. The `ordeq_spark.SparkCSV` does too, but the expected
    scheme is slightly different.

    There exist standards for resource specification, like file URIs or
    `fsspec`, but we cannot expect that we can derive the resource of the IO in
    this standard form. Sometimes the derivation is not straight-forward
    (consider an IO that accepts a glob as `path` - like
    `ordeq_polars.PolarsParquet`), and users that define custom IOs should not
    be obligated to derive the resource in this standard form.

    Because consistently inferring the used resource from the IO attributes is
    difficult, users should be able to explicitly define a resource, and set
    which IO instances share that resource:

    ```pycon
    >>> from ordeq import Resource
    >>> from ordeq_files import CSV
    >>> from ordeq_pandas import PandasCSV
    >>> from pathlib import Path
    >>> file = Resource()
    >>> csv_raw = file.add_io(
    ...     CSV(path=Path("path/to.csv"))
    ... )
    >>> csv_df = file.add_io(
    ...     PandasCSV(path="path/to.csv")
    ... )
    ```

    By adding the resource to both IOs, Ordeq knows that the resource is
    shared. This will be used when determining the topological ordering
    of nodes: each resource can be outputted by at most one node.

    An alternative, more syntactically pleasing way of setting the
    resource is as follows:

    ```pycon
    >>> file = Resource()
    >>> csv_raw = file // CSV(path=Path("path/to.csv"))
    >>> csv_df = file // PandasCSV(path="path/to.csv")
    ```

    Resources can have attributes. These attributes help represent the
    resource in the user's code, and can be reused to instantiate IOs:

    ```pycon
    >>> from ordeq import FileResource
    >>> file = FileResource(path=Path("path/to.csv"))
    >>> csv_raw = file // CSV(path=file.path)
    >>> csv_df = file // PandasCSV(path=str(file.path))
    ```

    Using resource attributes in the IO instantiation does not set the
    resource on the IO. For that we still need `file //` or
    `io.add_resource(file)`.

    Users can create custom resource classes too by subclassing from
    `Resource`:

    ```pycon
    >>> from ordeq import Resource
    >>> from ordeq_boto3 import S3Object
    >>> from dataclasses import dataclass
    >>> @dataclass(frozen=True)
    ... class S3File(Resource):
    ...     bucket: str
    ...     key: str
    >>> s3_file = S3File(bucket="bucket", key="key.csv")
    >>> csv_raw = s3_file // S3Object(
    ...     bucket=s3_file.bucket,
    ...     key=s3_file.key
    ... )
    >>> csv_df = s3_file // PandasCSV(
    ...     f"s3://{s3_file.bucket}/{s3_file.key}"
    ... )
    ```

    TODO: Nested IOs (IOs that use another IO as attribute) should
    theoretically inherit the resource of the attribute IO. (...)

    TODO: Sub-resources

    """

    def add_io(self, io: Tio) -> Tio:
        """Adds the IO to this resource.

        For practical reasons this actually appends this resource
        to the IO's `__resources__`, but this may change in the
        future.

        Args:
            io: The IO instance to add to this resource.

        Returns:
            The IO instance.
        """
        if not _has_resources(io):
            io.__dict__["__resources__"] = set()
        io.__dict__["__resources__"].add(self)
        return io

    def __matmul__(self, io: Tio) -> Tio:
        return self.add_io(io)

    def __floordiv__(self, io: Tio) -> Tio:
        return self.add_io(io)

    def __rshift__(self, io: Tio) -> Tio:
        return self.add_io(io)

    def __or__(self, io: Tio) -> Tio:
        return self.add_io(io)

    def __gt__(self, io: Tio) -> Tio:
        return self.add_io(io)


def get_resources(io: AnyIO) -> set[Any]:
    resources = set()
    if _has_resources(io):
        __resources__ = io.__resources__
        if callable(__resources__):
            resources = __resources__()
        else:
            resources = set(__resources__)
    if _has_references(io):
        for _, refs in io.references:
            for ref in refs:
                resources.add(*get_resources(ref))
    return resources
