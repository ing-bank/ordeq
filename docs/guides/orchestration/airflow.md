# Airflow

This guide demonstrates how to orchestrate an Ordeq pipeline using [Apache Airflow][airflow].
Airflow is a tool to programmatically author, schedule, and monitor workflows.
Ordeq is complementary to Airflow: while Airflow focuses on orchestration, Ordeq specializes in building modular and maintainable pipelines.

!!! tip "Familiarize yourself with running Ordeq projects"

    To get the most out of this guide, we recommend to familiarize yourself with running Ordeq projects.
    For instance, have a look at the [running guide][run-and-viz] if you haven't done so already.

The code examples presented in this section can be found [here][code-link].

## Example: air quality pipeline

We will use the air_quality pipeline as an example to demonstrate how to orchestrate an Ordeq pipeline using Airflow.
This pipeline ingests air quality data from an [external API][air-quality-api], processes it, and generates insights.
The example is adapted from the [Airflow docs][aq-example].

Let's inspect the project first:

=== "pipeline.py"

    ```python title=""
    --8<-- "examples/orchestration-airflow/src/air_quality/pipeline.py"
    ```

=== "catalog.py"

    ```python title=""
    --8<-- "examples/orchestration-airflow/src/air_quality/catalog.py"
    ```

=== "\_\_main\_\_.py"

    ```python title=""
    --8<-- "examples/orchestration-airflow/src/air_quality/__main__.py"
    ```

=== "Diagram"

    ```mermaid
    --8<-- "examples/orchestration-airflow/air_quality.mermaid"
    ```

=== "Example API response"

    ```json
    --8<-- "examples/orchestration-airflow/example-api-response.json"
    ```

The DAG consists of two nodes: `ingest` and `aggregate`.
The `ingest` node fetches air quality data from the API and stores it into a Parquet file.
The last tab shows an example response from this API.
The `aggregate` node computes statistics from the ingested data.

## Orchestrating with Airflow

This section will discuss three approaches to orchestrate the `air_quality` pipeline using Airflow.
If you want to follow along, first make sure to set up the Airflow environment using the instructions in the [README][airflow-example-readme].

!!! note "Airflow syntax"

    The code in this guide has been created for Airflow 3, and uses the TaskFlow API.
    The patterns and ideas apply to older Airflow versions as well, but the syntax may differ.
    Please refer to the [Airflow docs][pythonic-dags] for more information.

### Running individual nodes

The first approach to orchestrate an Ordeq pipeline with Airflow is to run each Ordeq node as an individual Airflow task.
Each task uses the `PythonOperator` to execute the corresponding Ordeq node.
The Airflow DAG for the air quality pipeline the looks as follows:

```python title=""
--8<-- "examples/orchestration-airflow/dags/dag_nodes.py"
```

Each task in the DAG corresponds to one Ordeq node.
The dependencies between the nodes are set using the `>>` operator.
This is needed because the `PythonOperator` does not automatically infer dependencies between tasks based on the Ordeq pipeline structure.

This approach is suitable when you want to have fine-grained control over the execution of each node and monitor their status individually.
Running node-by-node is less efficient than running the entire pipeline in a single task, as it incurs the overhead of task scheduling and context switching for each node.
This approach is also not suitable if a task produces outputs that are not persisted, as the subsequent task cannot access the in-memory outputs of the previous task.

### Running an entire pipeline

Instead of running each Ordeq node as an individual Airflow task, you can also run the entire Ordeq pipeline within a single Airflow task.
This approach uses the `PythonOperator` to execute the `run` function on the entire pipeline.
The Airflow DAG looks as follows:

```python title=""
--8<-- "examples/orchestration-airflow/dags/dag_pipeline.py"
```

This approach is more efficient than running node-by-node, but it sacrifices the fine-grained control and monitoring of individual nodes.
This approach most suitable when the pipeline is relatively small, and you want to keep the DAG simple.

### Running with Docker operator

The above approaches use the `PythonOperator` to run Ordeq nodes or pipelines within Airflow tasks.
This requires the Airflow environment to have all pipeline dependencies installed.
An alternative approach is to build a Docker image and run the container using the `DockerOperator`.

!!! note "Check out the Docker integration guide"

    If you are new to using Docker with Ordeq, check out the [Docker integration guide][docker] for more details on how to set up and use Docker with Ordeq.

The Airflow DAG can be defined as follows:

```python title=""
--8<-- "examples/orchestration-airflow/dags/dag_docker.py"
```

The `DockerOperator` takes the image and runs the Ordeq project inside the container.
The `command` parameter specifies the command to run inside the container, which in this case is to run the `air_quality` pipeline.
For more details on how to configure the Docker operator, please refer to the [Airflow documentation][docker-operator].

To run the DAG with Docker operator locally, you have to first build the image:

```shell
docker build -t air_quality_insights:latest .
```

Next, you can launch the Airflow environment and trigger the DAG from the UI.

[air-quality-api]: https://open-meteo.com/en/docs/air-quality-api
[airflow]: https://airflow.apache.org/
[airflow-example-readme]: https://github.com/ing-bank/ordeq/tree/main/examples/orchestration-airflow/README.md
[aq-example]: https://airflow.apache.org/docs/apache-airflow/stable/tutorial/objectstorage.html
[code-link]: https://github.com/ing-bank/ordeq/tree/main/examples
[docker]: ../integrations/docker.md
[docker-operator]: https://airflow.apache.org/docs/apache-airflow-providers-docker/stable/_api/airflow/providers/docker/operators/docker/index.html
[pythonic-dags]: https://airflow.apache.org/docs/apache-airflow/stable/tutorial/taskflow.html
[run-and-viz]: ../../guides/run_and_viz.md
