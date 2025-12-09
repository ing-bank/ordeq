import air_quality
import pendulum
from airflow.sdk import dag, task
from ordeq import run


@dag(
    dag_id="dag_pipeline",
    schedule="@daily",
    start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
)
def dag_pipeline():
    @task
    def task_run_pipeline(**kwargs):
        return run(air_quality)

    return task_run_pipeline()


_ = dag_pipeline()
