# Airflow orchestration example

To run the `air_quality` pipeline locally (without Airflow):

```shell
uv run -m air_quality
```

Or to visualize the pipeline:

```shell
uv run src/air_quality/viz.py
```

This will produce a visualization of the pipeline saved as `air_quality.mermaid`.

To spin up the Airflow environment locally:

```shell
export AIRFLOW_HOME=$(pwd)
export AIRFLOW__CORE__LOAD_EXAMPLES=0
export AIRFLOW__CORE__SIMPLE_AUTH_MANAGER_PASSWORDS_FILE=$(pwd)/creds.json
uv run airflow standalone
```

Retrieve the user and password from `creds.json.generated`.
Then, navigate to `http://localhost:8080` in your web browser to access the Airflow UI.

The Airflow DAGs are located in the `dags/` folder.
There are 3 DAGs available:

  - `dag_nodes.py`, which uses the PythonOperator and runs one Ordeq node in each Airflow task
  - `dag_pipeline.py`, which uses the PythonOperator and runs the entire Ordeq pipeline in a single Airflow task.
  - `dag_docker.py`, which uses the DockerOperator to run the Ordeq project.

To run the DAG with Docker operator, you have to first build the image:

```shell
docker build -t air_quality:latest .
```

Then, trigger the DAG from the Airflow UI.
