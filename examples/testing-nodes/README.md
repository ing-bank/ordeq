# Ordeq starter for testing nodes

This example demonstrates how to test nodes.
Testing nodes with Ordeq is simple and requires minimal overhead.
Nodes can be unit-tested like any other method, and tested using the dedicated testing utilities that Ordeq provides.
This project cannot be run individually.
To run its tests, run the following command from the current working directory:

```shell
uv run pytest
```

This will generate `tests-resources/txs-and-clients.csv` and `aggregated-txs.csv` while using `tests-resources/txs.csv` and `clients.csv` as input data.
