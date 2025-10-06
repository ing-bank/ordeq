import argparse
from typing import Any, TypeVar

from ordeq.framework.io import Input

T = TypeVar("T")


class CommandLineArg(Input[T]):
    """Dataset that represents a command line argument as node input. Useful
    for parameterization of node logic based on arguments in the run command.

    Parses the argument from `sys.argv` on load. See
    [argparse](https://docs.python.org/3/library/argparse.html) for more
    information.

    Example:

    ```python title="main.py"
    from ordeq import node, run
    from ordeq_spark import SparkHiveTable
    import pyspark.sql.functions as F
    from pyspark.sql import DataFrame


    @node(
        inputs=[SparkHiveTable(table="my.table"), CommandLineArg("--value")],
        outputs=SparkHiveTable(table="my.output"),
    )
    def transform(df: DataFrame, value: str) -> DataFrame:
        return df.where(F.col("col") == value)


    if __name__ == "__main__":
        run(transform)
    ```

    When you run `transform` through the CLI as follows:

    ```shell
    python main.py --value MyValue
    ```

    `MyValue` will be used as `value` in `transform`.

    By default, the command line arguments are parsed as string. You can
    parse as different type using built-in type converters, for instance:

    ```python
    import pathlib
    import datetime

    k = CommandLineArg("--k", type=int)
    threshold = CommandLineArg("--threshold", type=float)
    address = CommandLineArg("--address", type=ascii)
    path = CommandLineArg("--path", type=pathlib.Path)
    date_time = CommandLineArg("--date", type=datetime.date.fromisoformat)

    ```

    Alternatively, you can parse using a user-defined function, e.g.:

    ```python
    def hyphenated(string: str) -> str:
        return "-".join([w[:4] for w in string.casefold().split()])


    title = CommandLineArg("--title", type=hyphenated)
    ```

    When using multiple `CommandLineArg` IOs in a node, then you can link them
    to the same argument parser:

    ```python
    import argparse

    parser = argparse.ArgumentParser()
    arg1 = CommandLineArg("--arg1", parser=parser)
    arg2 = CommandLineArg("--arg2", parser=parser)
    ```

    Parsing command line arguments as `argparse.FileType` is discouraged as
    [it has been deprecated](https://docs.python.org/3.14/whatsnew/3.14.html#deprecated)
    from Python 3.14.

    More info on parsing types [here](https://docs.python.org/3/library/argparse.html#type)
    """

    arg: str
    kwargs: dict[str, Any]
    parser: argparse.ArgumentParser

    def __init__(
        self, arg: str, parser: argparse.ArgumentParser | None = None, **kwargs
    ):
        super().__init__()
        self.parser = parser or argparse.ArgumentParser()
        self.parser.add_argument(arg, **kwargs)
        # Storing the argument and kwargs for object description
        self.arg = arg
        self.kwargs = kwargs

    def load(self) -> T:
        ns, _ = self.parser.parse_known_args()
        _, val = vars(ns).popitem()
        return val

    def __repr__(self):
        return f"CommandLineArg(arg={self.arg}, kwargs={self.kwargs})"
