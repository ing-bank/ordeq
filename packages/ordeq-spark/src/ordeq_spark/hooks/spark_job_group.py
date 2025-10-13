from ordeq import Node, NodeHook

from ordeq_spark.utils import get_spark_session


def _set_job_group(name: str) -> None:
    get_spark_session().sparkContext.setJobGroup(name, name)


class SparkJobGroupHook(NodeHook):
    """Node hook that sets the Spark job group to the node name.
    Please make sure the Spark session is initialized before using this hook.

    Example usage:

    ```pycon
    >>> from ordeq import node, run
    >>> from ordeq_spark import SparkHiveTable
    >>> from pyspark.sql import DataFrame

    >>> @node(
    ...     inputs=SparkHiveTable(table="tables.a"),
    ...     outputs=SparkHiveTable(table="tables.b"),
    ... )
    ... def append(a: DataFrame) -> DataFrame:
    ...     return a.union(a)

    >>> run(append, hooks=[SparkJobGroupHook()]) # doctest: +SKIP

    ```

    """

    def before_node_run(self, node: Node) -> None:
        """Sets the node name as the job group in the Spark context.
        This makes the history server a lot easier to use.

        Args:
            node: the node

        Raises:
            RuntimeError: if the Spark session is not active
        """  # noqa: DOC502 (docstring-extraneous-exception)

        _set_job_group(node.name)
