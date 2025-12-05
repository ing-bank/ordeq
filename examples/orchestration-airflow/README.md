# Airflow orchestration example

To run the `air_quality` pipeline locally (without Airflow):

```shell
uv run -m air_quality_insights
```

To spin up the Airflow environment locally:

```shell
docker compose up
```

Access the password at `airflow/.env` file.

Then, navigate to `http://localhost:8080` in your web browser to access the Airflow UI.